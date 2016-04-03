import urllib3
start = 1
end = 27
step = 1
link = 'insert url link ending in /<number>'
for i in range(start, end, step):
    url = link + str(i)+ '.jpg'
    connection_pool = urllib3.PoolManager()
    resp = connection_pool.request('GET',url )
    f = open(str(i)+'.jpg', 'wb')
    f.write(resp.data)
    f.close()
    resp.release_conn()

