demo_get_url = http://nj.meituan.com/meishi/pn32/

请求后抓包： 这个是get 具体的的地址
http://nj.meituan.com/meishi/api/poi/getPoiList?cityName=%E5%8D%97%E4%BA%AC&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=32&userId=&uuid=3c85d8393756482db854.1533021451.1.0.0&platform=1&partner=126&originUrl=http%3A%2F%2Fnj.meituan.com%2Fmeishi%2Fpn32%2F&riskLevel=1&optimusCode=1&_token=eJx9UN1ugjAYfZfeSqQtFajJLmBjoG4qwia67AKlAiKVQQXisndfl7iL3Sz5mvPznZy0%2FQT1JAFjBCGFUAEtq8EYoCEc6kABopGbkaZBTBAdUaIpYP%2FH0yGW3q5%2BfQDjNwpNxdDI%2B4%2BxkvpNxnTF1KVzo1h%2FVzCR85OZyAjIhKjGqsqPw5Ll4hLz4f5cqpI3Wa5WXMOqvMa%2FISC7ylB2SSxuGN9Q%2FOpn%2BShZ1OQpl4xNu9MxRAvr6viryyDoPtZUiCTzo5n9krtZYl8t%2BStF11Ye0ZziofDm0zC1R%2BTR2DgeatlTyAxhObaec9OP3SWxBwxunDY%2FUKK2NTRXz2uW%2BoNya4xO1cEJquOs1HzCUxHkztTsl2JZXPcGCmcnWlgXnzWn%2FunlvNy5r9Ec5dmq60pzvl5MM7qtmz5B92ofzCwYbSJBs3vRpKjJ6MdEG7gtPgpvl0SPfbM74P6i8X4fyoOCBW74GTNebeOQe7HKCzRx07s78PUNP7qZAw%3D%3D
主要矛盾在 _token 这个值的生成  其他值基本不用考虑


生成token 的方法：
d = window.Rohr_Opt.reload(p)
p 可为任何值