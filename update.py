'''update a brand'''
def update_brand(request,brand_id):
    #print 'request',request.POST
    brand_id=brand_id
    con = psycopg2.connect("dbname='vuevent' user='postgres' password='silver'") 
    cur = con.cursor()
    for brands in Brand.objects.raw('SELECT id,brand_name,brand_logo,brand_image,interest_tags FROM brands_brand WHERE id = %s', [brand_id]):
        brand_name=brands.brand_name
        brand_logo=brands.brand_logo
        brand_image=brands.brand_image
        interest_tags=brands.interest_tags
    #print 'here sachin', brand_name,brand_logo,brand_image,interest_tags
    if request.POST['brand_name']:
        brand_n=request.POST['brand_name'],
        brand_name_new=''.join(brand_n)
    else:
        brand_name_new=brand_name
    if request.POST['brand_image']:
        r_logo1=request.POST['brand_image']
        split_logo1=r_logo1.partition(',')
        b64_str1=split_logo1[2]
        image_name=request.POST['brand_image_name'],
        brand_image_name1=''.join(image_name)
        brand_img_split=brand_image_name1.partition('.')
        brand_image_name=brand_img_split[0]
        image_save_path="/files/assets/images/brand-image/"
        fh1 = open("files/assets/images/brand-image/"+brand_image_name+'.png', "wb")
        fh1.write(b64_str1.decode('base64'))
        image_file_path=image_save_path+brand_image_name+'.png'
        brand_image=image_file_path
        fh1.close()
    else:
        brand_image=brand_image
    if request.POST['brand_logo']:
        r_logo=request.POST['brand_logo']
        split_logo=r_logo.partition(',')
        b64_str=split_logo[2]
        logo_name=request.POST['brand_logo_name'],
        brand_logo_name1=''.join(logo_name)
        brand_log_split=brand_logo_name1.partition('.')
        brand_logo_name=brand_log_split[0]
        logo_save_path="/files/assets/images/brand-logo/"
        fh = open('files/assets/images/brand-logo/'+brand_logo_name+'.png', "wb")
        fh.write(b64_str.decode('base64'))
        logo_file_path=logo_save_path+brand_logo_name+'.png'
        brand_logo=logo_file_path
        fh.close()
    else:
        brand_logo=brand_logo
    if request.POST['interest_tags']:
        tags=request.POST['interest_tags']
        tags_new=json.loads(tags)
        interest_tag=[d['name'] for d in tags_new]
        str1 = ','.join(interest_tag)
        interest_tags=str(str1)
    else:
        interest_tags=interest_tags
    cur.execute("UPDATE brands_brand SET brand_name=%s,brand_image=%s,brand_logo=%s,interest_tags=%s WHERE id=%s", (brand_name_new,brand_image,brand_logo,interest_tags, brand_id))        
    con.commit()

    url='/brand/info'+'/'+brand_id+'/'
    print 'url>>>>',url
    return HttpResponseRedirect(url)
