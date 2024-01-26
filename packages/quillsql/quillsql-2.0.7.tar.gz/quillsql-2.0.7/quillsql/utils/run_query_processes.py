import json


def get_table_schema(query_results, target_pool):
  target_pool.query(query_results[0])
  types_query = target_pool.query(
      "select typname, oid, typarray from pg_type order by oid;"
  )
  cursor = target_pool.cursor()
  fields = [{"name": desc[0], "dataTypeID": desc[1]} for desc in cursor.description]
  schema = [
                {
                    "fieldType": next(
                        (
                            dict(type)["typname"]
                            for type in types_query
                            if field["dataTypeID"] == dict(type)["oid"]
                        ),
                        None,
                    ),
                    "name": field["name"],
                    "displayName": field["name"],
                    "isVisible": True,
                }
                for field in fields
            ]

  return schema

def remove_fields(query_result, cursor_description, fields_to_remove):
  fields = [
      {"name": desc[0], "dataTypeID": desc[1]}
      for desc in cursor_description
      if desc[0] in fields_to_remove
  ]
  rows = [dict(json.loads(json.dumps(row, default=str))) for row in query_result]

  for row in rows:
    for field in fields_to_remove:
      if field in row:
          del row[field]
  return {fields, rows}

def array_to_map(queries, array_to_map, metadata, target_pool):
  for i in range(len(queries)):
    query_result = target_pool.query(queries[i])
    metadata[array_to_map.get("arrayName")][i][array_to_map.get("field")] = query_result.get("rows")
