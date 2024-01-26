import os
from dotenv import load_dotenv

from psycopg2.extensions import make_dsn
import requests
import redis


from src.db.cached_pool import CachedPool
from src.utils.run_query_processes import array_to_map, get_table_schema, remove_fields

load_dotenv()

ENV = os.getenv("PYTHON_ENV")
DEV_HOST = "http://localhost:8080"
PROD_HOST = "https://quill-344421.uc.r.appspot.com"
HOST = DEV_HOST if ENV == "development" else PROD_HOST

## Quill - Fullstack API Platform for Dashboards and Reporting.
class Quill:
    def __init__(self, private_key, 
        database_connection_string="",
        psycopg2_connection=None, cache=None):
        # Handles both dsn-style connection strings (eg. "dbname=test password=secret" )
        # as well as url-style connection strings (eg. "postgres://foo@db.com")
        to_dsn = lambda conn: make_dsn(conn) if "://" in conn else conn
        self.database_connection_string = to_dsn(database_connection_string)
        self.target_pool = CachedPool(
            database_connection_string, cache, psycopg2_connection
        )
        self.private_key = private_key

    def get_cache(self, cache_config):
        cache_type = cache_config and cache_config.get("cache_type")
        if cache_type and cache_type == "redis" or cache_type == "rediss":
            return redis.Redis(
                host=cache_config.get("host", "localhost"),
                port=cache_config.get("port", 6379),
                username=cache_config.get("username", "default"),
                password=cache_config.get("password"),
            )
        return None

    def query(self, org_id, data):
        metadata = data.get("metadata")
        if not metadata:
            return {"error": "400", "errorMessage": "Missing metadata."}

        task = metadata.get("task")
        if not task:
            return {"error": "400", "errorMessage": "Missing task."}
        
        try:
            pre_query_results = self.run_queries(metadata.get("preQueries")) # used by the view task to get non-sensitive data
            payload = {**metadata, "orgId": org_id, "preQueryResults" : pre_query_results}
            quill_results = self.post_quill(metadata.get("task"), payload)
            # If there is no metedata in the quill results, create one
            if not quill_results.get("metadata"):
                quill_results["metadata"] = {}
            metadata = quill_results.get("metadata")
            final_query_results = self.run_queries(quill_results.get("queries"), metadata, metadata.get("runQueryConfig"))
            # Quick hack to make the sdk work with the Frontend
            if len(final_query_results.get("queryResults")) == 1:
                query_result = final_query_results.get("queryResults")[0]
                quill_results["metadata"]["rows"] = query_result.get("rows")
                quill_results["metadata"]["fields"] = query_result.get("fields")
            return {"data": quill_results.get("metadata"), "queries": final_query_results, "status": "success"}

        except Exception as err:
            return {"error": str(err), "status": "error"}
        
    def run_queries(self, queries, metadata=None, runQueryConfig=None):
        results = {}
        if not queries:
            return {'queryResults': []}
        if runQueryConfig and runQueryConfig.get("arrayToMap"):
            array_to_map(queries, runQueryConfig.get("arrayToMap"), metadata, self.target_pool)
            return {'queryResults': []}
        else:
            query_results = [self.target_pool.query(query) for query in queries]
            results['queryResults'] = query_results
            if runQueryConfig and runQueryConfig.get("getSchema"):
                results['columns'] = get_table_schema(query_results, self.target_pool)
            if runQueryConfig and runQueryConfig.get("removeFields"):
                results['queryResults'] = remove_fields(query_results, runQueryConfig.get("removeFields"))
        
        return results
        
    def post_quill(self, path, payload):
        url = f"{HOST}/sdk/{path}"
        headers = {"Authorization": f"Bearer {self.private_key}"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
