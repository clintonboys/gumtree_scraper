for node in gt_li:
    if len(node.contents) > 0:
        post_dict={}
        if node.findAll('a') is not None:
            post_dict['title']=node.findAll('a')[0].string
        if node.find('div',attrs={"class":"h-elips"}) is not None:
            post_dict['price']=node.find('div',attrs={"class":"h-elips"}).string
        if node.findAll('span') is not None:
            post_dict['description']=node.findAll('span')[0].contents[0]
        if node.find('h3',attrs={"class":"rs-ad-location"}) is not None:
            post_dict['location1']=node.find('h3',attrs={"class":"rs-ad-location-area"}).contents[0]
        if node.find('span',attrs={"class":"rs-ad-location-suburb"}) is not None:
            post_dict['location2']=node.find('span',attrs={"class":"rs-ad-location-suburb"}).contents[0]
        if node.find('div',attrs={"class":"rs-ad-date"}) is not None:
            post_dict['date']=node.find('div',attrs={"class":"rs-ad-date"}).contents[0]
        anchors=node.findAll('a')
        for node in anchors:
            if node.get("data-adid") is not None:
                post_dict['ad_id']=node.get('data-adid')
        master_list.append(post_dict)
