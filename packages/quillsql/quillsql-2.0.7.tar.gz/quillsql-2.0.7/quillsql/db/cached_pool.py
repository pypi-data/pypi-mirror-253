import psycopg2
import psycopg2.extras
import json
import redis
from src.error import PgQueryError

## The TTL for new cache entries (default: 1h)
DEFAULT_CACHE_TTL = 24 * 60 * 60

class CachedPool:
    def __init__(self, config, cache_config, psycopg2_connection=None):
        if psycopg2_connection:
            self.pool = psycopg2_connection
        else:
            self.pool = psycopg2.connect(config)
        self.cache = self.get_cache(cache_config)
        self.ttl = cache_config and cache_config.get("ttl") or DEFAULT_CACHE_TTL
        self.cur = self.pool.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        self.orgId = None

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

    def cursor(self):
        return self.cur

    def exec(self, sql):
        try:
          self.cur.execute(sql)
        except psycopg2.Error as err:
          raise PgQueryError(err, sql, err.diag.statement_position)
        fetch =  self.cur.fetchall()
        fields = [{"name": desc[0], "dataTypeID": desc[1]} for desc in self.cur.description]
        return {'rows': fetch, 'fields': fields}

    def query(self, sql):
        if not self.cache:
            return self.exec(sql)

        key = f"{self.orgId}:{self.sql}"
        cached_result = self.cache.get(key)
        if cached_result:
            cached = json.loads(cached_result)
            fields = [{"name": desc[0], "dataTypeID": desc[1]} for desc in self.cur.description]
            return {'rows': cached, 'fields': fields}
        else:
            new_result = self.exec(sql)
            new_result_string = json.dumps(new_result)
            self.cache.set(key, new_result_string, "EX", DEFAULT_CACHE_TTL)
            fields = [{"name": desc[0], "dataTypeID": desc[1]} for desc in self.cur.description]
            return {'rows': new_result, 'fields': fields}