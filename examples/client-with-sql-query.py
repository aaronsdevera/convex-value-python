from convexvalue import ConvexValue

cvx = ConvexValue()

SQL_QUERY = '''select
  *
  from opt_summary
  where symbol like '.SPX%'
  limit 50
'''

results = cvx.query_sql(SQL_QUERY)

print(results.plot())