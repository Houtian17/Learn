from redis import StrictRedis

if __name__ == '__main__':
    # 创建一个StrictRedis对象，连接redis数据库
    try:
        sr = StrictRedis()
        # 添加一个key，为name，value，hbzb
        # res = sr.set('name', 'hbzb')

        # 修改name的值为xjf
        res = sr.set('name', 'xjf')
        print(res)

        # 获取name的值
        res = sr.get('name')
        print(res)
    except Exception as e:
        print(e)
