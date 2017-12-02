

########### Python 2.7 #############
import httplib, urllib, base64,cv2,thread
import json

cap = cv2.VideoCapture(0)
fear=0
anger=0
gender=''

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

def calling_api(img1):
    global fear,anger
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '094653d420844c7ca34841c000788995',
    }

    params = urllib.urlencode({
    })


    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, img1.read(), headers)
    response = conn.getresponse()
    data = response.read()
    data_json = json.loads(data[1:-1])
    '''
    for i in data_json[u'scores'].keys():
        print(str(i),':',data_json[u'scores'][i])
        '''

    conn.close()
    fear,anger = data_json[u'scores'][u'fear'], data_json[u'scores'][u'anger']
def calling_api_gender(img1):
    uri_base = 'westcentralus.api.cognitive.microsoft.com'

    # Request headers.
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '657d4b8581ad422baca1a26bd9371551',
    }

    # Request parameters.
    params = urllib.urlencode({
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,emotion',
    })


    
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, img1.read(), headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
i=1
while True:
    ret, img = cap.read()
    
    # cv2.waitKey(0)
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.8, 5)
    for kk,(x,y,w,h) in enumerate(faces):
        #print(w*h)
        #if w*h > 6500:
        img_sv = img[y:y+h, x:x+w]
        cv2.imwrite('x.jpg', img_sv)
        img1 = open('x.jpg', 'rb')
        stt = str(x)+','+str(y)+','+str(w)+','+str(h)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.imshow('image.jpg',img)
        # cv2.putText(img, face ,(x, y-20), font, .5,(255,255,255),2,cv2.CV_AA)
        if i%100 == 0:
            # thread.start_new_thread(calling_api_emotion, (img1,) )
            thread.start_new_thread(calling_api_gender, (img1,) )
            # calling_api(img1,stt)
    i+=1
    i=i%100
    # print(i)
    cv2.imwrite('xx.jpeg', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

####################################
'''
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64,cv2

cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX


def calling_api(img):
    headers = {
        # Request headers
        'Content-Type': 'multipart/form-data',
        'Ocp-Apim-Subscription-Key': '{e90d04cabe1548c9ac8745f1479fd281}',
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?faceRectangles={faceRectangles}&%s" % params, img.read(), headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
'''
