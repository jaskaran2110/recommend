import subprocess
import sys
from flask import Flask, request
import pandas as pd

# import cv2
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json

import numpy as np


@app.route("/", methods=["GET", "POST"])
def index():
    output = request.get_json()

    age = int(output['age'])
    insulin = int(output['insulin_amount'])
    weight = float(output['weight'])
    meal = str(output['diet'])
    diabetic = output['class']
    gender = output['gender']
    kidney = int(output['chronic_kidney'])
    hyper = int(output['hypertension'])
    heart = int(output['heart'])
    sbp = int(output['systolic_bp'])
    data_str = []

    if weight <= 36:
        if kidney == 1:
            data_str = "Water recommended for you is 8 glasses due to chronic kidney damage."
        elif insulin == 0:
            data_str = "Normal Water recommended for you is 6 glasses. GO for hydration"
        else:
            data_str = "Normal Water recommended for you is 7 glasses due to insulin"
    elif weight <= 56:
        if kidney == 1:
            data_str = "Water recommended for you is 9 glasses due to chronic kidney damage."
        elif insulin == 0:
            data_str = "Normal Water recommended for you is 7 glasses. GO for hydration"
        else:
            data_str = "Normal Water recommended for you is 8 glasses due to insulin"

    elif weight <= 76:
        if kidney == 1:
            data_str = "Water recommended for you is 10 glasses due to chronic kidney damage."
        elif insulin == 0:
            data_str = "Normal Water recommended for you is 8 glasses. GO for hydration"
        else:
            data_str = "Normal Water recommended for you is 9 glasses due to insulin"

    elif weight <= 90:
        if kidney == 1:
            data_str = "Water recommended for you is 11 glasses due to chronic kidney damage."
        elif insulin == 0:
            data_str = "Normal Water recommended for you is 9 glasses. GO for hydration"
        else:
            data_str = "Normal Water recommended for you is 10 glasses due to insulin"
    else:
        if kidney == 1:
            data_str = "Water recommended for you is 12 glasses due to chronic kidney damage."
        elif insulin == 0:
            data_str = "Normal Water recommended for you is 10 glasses. GO for hydration"
        else:
            data_str = "Normal Water recommended for you is 11 glasses due to insulin"

    data1 = {"description" : data_str}
    # Meal
    # if meal== 'veg':
    #     if diabetic == 'non_diabetic':
    #         pass
    #     else:
    #         pass
    # else:
    #     if diabetic == 'non_diabetic':
    #         pass
    #     else:
    #         pass

    # Fruits
    if hyper == 1:
            desc2 = "Fruits helping in controlling blood pressure"
            val1 = {"name":"Apricots", "imgUrl" : "https://img.freepik.com/premium-photo/ripe-apricot-fruits-with-with-green-leaf-slice-isolated_80510-455.jpg?w=996"}
            val2 = {"name":"Bananas", "imgUrl":"https://assets.shop.loblaws.ca/products/20175355001/b3/en/front/20175355001_front_a06_@2.png"}
            val3 = {"name":"Kiwi", "imgUrl":" https://cdn.britannica.com/45/126445-050-4C0FA9F6/Kiwi-fruit.jpg"}
            val4 = {"name":"Pomengrate", "imgUrl":" https://img.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2014/01/10/Production/Health/Images/bigstock-Half-of-pomegranate-on-a-white-12359999.jpg?uuid=V__-xHohEeOJY7S2VLzJsg"}

    elif insulin == 0:
            desc2 = "Try to eat fibre rich fruits"
            val1 = {"name": "Orange", "imgUrl": "https://5.imimg.com/data5/SELLER/Default/2021/12/TH/KH/HD/134286407/fresh-orange-500x500.jpg"}
            val2 = {"name": "Guava", "imgUrl": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F19%2F2020%2F01%2F02%2F429048911_6119360327001_6119354197001-vs.jpg"}
            val3 = {"name": "Apples", "imgUrl": "https://static.libertyprim.com/files/familles/pomme-large.jpg?1569271834"}
            val4 = {"name":"Bananas", "imgUrl":"https://assets.shop.loblaws.ca/products/20175355001/b3/en/front/20175355001_front_a06_@2.png"}

    else:
            desc2  = "Insulin friendly fruits that will help you"
            val1 = {"name": "Papaya", "imgUrl": "https://cdn.shopify.com/s/files/1/0018/4421/5860/products/PapayaRipe_590x.jpg?v=1592404724"}
            val2 = {"name": "Berries", "imgUrl": "https://cdn3.creativecirclemedia.com/keypennews/original/20210526-151237-21_06-KP-Cooks-berries-ol.jpg"}
            val3 = {"name": "Apples", "imgUrl": "https://static.libertyprim.com/files/familles/pomme-large.jpg?1569271834"}
            val4 = {"name": "Peaches", "imgUrl": "https://billsberryfarm.com/wp-content/uploads/2020/08/peach.png"}


    data2 = {"description" : desc2, "items" : [val1,val2,val3,val4]}

    if heart == 1:
        data_str3 = "No smoking is recommended due to cardiovascular disease"
    elif hyper == 1:
        data_str3 = "Limit Cigarettes to 1 due to high blood pressure"
    elif insulin == 1:
        data_str3 = "Consult with your doctor before smoking as you may need high doses of insulin"
    else:
        data_str3 = "No complications but avoid smoking"

    data3 = {"description": data_str3}
    data4 = {}
    if sbp < 121:
        pass
    elif sbp < 140:
        data4 = {"description": "You are at risk of hypertension. Follow our recommended diet"}
    else:
        data4 = {"description": "High risk of hypertension. Consult a doctor"}

    if heart == 1:
        data_str5 = "Limit drinking to one drink a day due to cardiovascular disease"
    elif hyper == 1:
        data_str5 = "Avoid drinking due to high blood pressure"
    elif insulin == 1:
        if gender == "female":
            data_str5 = "Can drink in moderation with insulin -  1 drinks per day for women"
        else:
            data_str5 = "Can drink in moderation with insulin -  2 drinks per day for men"

    else:
        if gender == "female":
            data_str5 = "No complications but drink in moderation - 1 drinks per day for women "
        else:
            data_str5 = "No complications but drink in moderation - 2 drinks per day for men "

    data5 = {"description": data_str5}

    item0 = [ ]

    if age <20:
        item0.append({"activity": "Young age - can explore sports and gymnastics", "imgUrl": ""})
        item0.append({"activity": "resistance exercises with exercise bands or weights", "imgUrl": ""})
    elif age<30:
        if gender == 'female':
            item0.append({"activity": "Young female - 30 minutes of aerobic exercise a day", "imgUrl": ""})
            item0.append({"activity": "Do cycling and running while building muscle and strengthen bone density", "imgUrl": ""})
        else:
            item0.append({"activity": "Young male - 30 minutes of aerobic exercise a day", "imgUrl": ""})
            item0.append({"activity": "Work on flexibility and increased weight training", "imgUrl": ""})

    elif age < 40:
        if gender == 'female':
            item0.append({"activity": "One hour of circuit training (cardio and resistance) 4x a week", "imgUrl": "https://www.shape.com/thmb/b6IZDem4RRtzEGd8jJIWYiv2nsY=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/benefits-of-circuit-training-workout-82955b2e1b6144d6b50789109b0eea5e.jpg"})
            item0.append({"activity": "one day  Interval-based cardio like spinning for 45 to 60 minutes", "imgUrl": ""})

        else:
            item0.append({"activity": "One hour of circuit training (cardio and resistance) 4x a week", "imgUrl": "https://www.shape.com/thmb/b6IZDem4RRtzEGd8jJIWYiv2nsY=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/benefits-of-circuit-training-workout-82955b2e1b6144d6b50789109b0eea5e.jpg"})
            item0.append({"activity": "one day  cardio for 45 to 60 minutes", "imgUrl": ""})
            item0.append({"activity": "Work on all your muscle groups", "imgUrl": ""})

    elif age < 50:
        if gender == 'female':
            item0.append({"activity": "One hour of cardio training 3 days a week", "imgUrl": ""})
            item0.append({"activity": "Strengthen your muscles on days in between", "imgUrl": ""})

        else:
            item0.append({"activity": "One hour of weight training 3 days a week", "imgUrl": ""})
            item0.append({"activity": "45 minutes of cardio five days a week", "imgUrl": ""})
    elif age < 60:
        if gender == 'female':
            item0.append({"activity": "20 minutes of weight training 4 days a week", "imgUrl": "https://blogscdn.thehut.net/wp-content/uploads/sites/478/2018/08/22104341/Blog-Squattingwithbarbell-Female_700x385.jpg"})
            item0.append({"activity": "Emphasize resistance training to improve bone density", "imgUrl": "https://prod-ne-cdn-media.puregym.com/media/804662/trx_blog.jpg?quality=80&mode=pad&width=992"})

        else:
            item0.append({"activity": "20 minutes of weight training 4 days a week", "imgUrl": "https://www.bodybuilding.com/images/2019/july/best-beginner-weight-training-guide-with-easy-to-follow-workout-header-b-830x467.jpg"})
            item0.append({"activity": "Put time into resistance training", "imgUrl": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/athlete-man-doing-gymnastic-exercises-to-strength-royalty-free-image-1647016002.jpg?crop=1.00xw:0.891xh;0,0.109xh&resize=640:*"})

    else:
        item0.append({"activity": "Light activities such as yoga, walking, gardening, and cleaning", "imgUrl": "https://hips.hearstapps.com/hmg-prod/images/woman-watering-flowers-in-garden-with-watering-can-royalty-free-image-137086506-1555439151.jpg?crop=0.705xw:1.00xh;0.0622xw,0&resize=768:*"})
        item0.append({"activity": "Take plenty of time to warm up, cool down, and rest between sets", "imgUrl": "https://thumbs.dreamstime.com/b/blackouts-senior-man-bike-exercise-gym-blackouts-senior-man-bike-exercise-gym-exhausted-blackouts-senior-man-165458644.jpg"})

    data6 = {"description" : 'Follow this workout schedule according to your age', "items" : item0}

    item = []
    if meal == 'nonveg':
        if weight < 50:
            item.append({ "Lean Proteins Non Veg for diabetic underweight": " 250 gm Chicken Breast", "imgUrl": "https://dao54xqhg9jfa.cloudfront.net/OMS-ProductMerchantdising/d49aac35-6784-73e1-93ff-ac738c240f15/original/Chicken-Breast-Boneless-(3-4-Pieces)-Hero-Shot_(1).jpg?format=webp"})
        elif weight <80:
            item.append({"Lean Proteins Non Veg for diabetic moderate": "300 gm Chicken Breast", "imgUrl": "https://dao54xqhg9jfa.cloudfront.net/OMS-ProductMerchantdising/d49aac35-6784-73e1-93ff-ac738c240f15/original/Chicken-Breast-Boneless-(3-4-Pieces)-Hero-Shot_(1).jpg?format=webp"})
        else:
            item.append({"Lean Proteins Non Veg for diabetic overweight": "350 gm Chicken Breast", "imgUrl": "https://dao54xqhg9jfa.cloudfront.net/OMS-ProductMerchantdising/d49aac35-6784-73e1-93ff-ac738c240f15/original/Chicken-Breast-Boneless-(3-4-Pieces)-Hero-Shot_(1).jpg?format=webp"})

    else:
        if weight < 50:
            item.append({"Lean Protein Veg for underweight": " 20 gm Soya chunks", "imgUrl": "https://www.healthshots.com/wp-content/uploads/2020/05/soya-chunks-370x207.jpg"})
        elif weight < 80:
            item.append({"Lean Protein Veg for moderate": "25 gm Soya chunks", "imgUrl": "https://www.healthshots.com/wp-content/uploads/2020/05/soya-chunks-370x207.jpg"})
        else:
            item.append({"Lean Protein Veg for overweight": "35 gm Soya chunks", "imgUrl": "https://www.healthshots.com/wp-content/uploads/2020/05/soya-chunks-370x207.jpg"})

    if insulin == 1:
        item.append({"Recommended Whole grains for patients taking insulin": "Whole wheat, Brown rice", "imgUrl": "https://www.narayanahealth.org/blog/wp-content/uploads/2022/03/Brown-Rice-Image.jpeg"})


    if heart == 1:
        item.append({"Recommendation":"Eat leafy green vegetable to make heart healthy", "imgUrl": "https://www.verywellfit.com/thmb/z5TVh8sYWjbpRf226Xb9JDaYNBM=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/greens-f0499a942c2b48078200a0a1b0ec0f6c.jpg"})

    if hyper==1:
        item.append({"Recommendation":"Limit intake of salt to 5 Grams per day due to hypertension complications", "imgUrl": "https://cdn-prod.medicalnewstoday.com/content/images/articles/310/310977/man-picking-up-salt-shaker.jpg"})

    # if hyper == 1:
    #         desc2 = "Fruits helping in controlling blood pressure"
    #         val1 = {"name":"Apricots", "imgUrl" : "https://img.freepik.com/premium-photo/ripe-apricot-fruits-with-with-green-leaf-slice-isolated_80510-455.jpg?w=996"}
    #         val2 = {"name":"Bananas", "imgUrl":"https://assets.shop.loblaws.ca/products/20175355001/b3/en/front/20175355001_front_a06_@2.png"}
    #         val3 = {"name":"Kiwi", "imgUrl":" https://cdn.britannica.com/45/126445-050-4C0FA9F6/Kiwi-fruit.jpg"}
    #         val4 = {"name":"Pomengrate", "imgUrl":" https://img.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2014/01/10/Production/Health/Images/bigstock-Half-of-pomegranate-on-a-white-12359999.jpg?uuid=V__-xHohEeOJY7S2VLzJsg"}
    #
    # elif insulin == 0:
    #         desc2 = "Try to eat fibre rich fruits"
    #         val1 = {"name": "Orange", "imgUrl": "https://5.imimg.com/data5/SELLER/Default/2021/12/TH/KH/HD/134286407/fresh-orange-500x500.jpg"}
    #         val2 = {"name": "Guava", "imgUrl": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F19%2F2020%2F01%2F02%2F429048911_6119360327001_6119354197001-vs.jpg"}
    #         val3 = {"name": "Apples", "imgUrl": "https://static.libertyprim.com/files/familles/pomme-large.jpg?1569271834"}
    #         val4 = {"name":"Bananas", "imgUrl":"https://assets.shop.loblaws.ca/products/20175355001/b3/en/front/20175355001_front_a06_@2.png"}
    #
    # else:
    #         desc2  = "Insulin friendly fruits that will help you"
    #         val1 = {"name": "Papaya", "imgUrl": "https://cdn.shopify.com/s/files/1/0018/4421/5860/products/PapayaRipe_590x.jpg?v=1592404724"}
    #         val2 = {"name": "Berries", "imgUrl": "https://cdn3.creativecirclemedia.com/keypennews/original/20210526-151237-21_06-KP-Cooks-berries-ol.jpg"}
    #         val3 = {"name": "Apples", "imgUrl": "https://static.libertyprim.com/files/familles/pomme-large.jpg?1569271834"}
    #         val4 = {"name": "Peaches", "imgUrl": "https://billsberryfarm.com/wp-content/uploads/2020/08/peach.png"}


    data7 = {"description" : 'Follow this dietplan according to your complications', "items" : item}

    # block, _ = subprocess.Popen([sys.executable, "tiff.py", str(lat) + "," + str(long)],
    #                             stdout=subprocess.PIPE).communicate()
    # j = json.loads(block)
    #
    #
    #
    # combined = {"hospital": jsonstring3, "hotel": jsonstring, "Places": jsonstring2, "Budget": budget}
    #
    # # print((jsonstring))
    # # print(type(jsonstring2))
    # #

    return {"data":[data1,data2, data3,data4,data5,data6, data7]}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2000)
