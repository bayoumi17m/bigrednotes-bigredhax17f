########### Python 2.7 #############
import httplib, urllib, base64, time, json, os

def justDoIt():
    ###############################################
    #### Update or verify the following values. ###
    ###############################################

    # Replace the subscription_key string value with your valid subscription key.
    subscription_key = 'd101f6aafa5c44208ead247cfb3d8b32'

    # Replace or verify the region.
    #
    # You must use the same region in your REST API call as you used to obtain your subscription keys.
    # For example, if you obtained your subscription keys from the westus region, replace
    # "westcentralus" in the URI below with "westus".
    #
    # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
    # a free trial subscription key, you should not need to change this region.
    uri_base = 'eastus2.api.cognitive.microsoft.com'

    headers = {
        # Request headers.
        # Another valid content type is "application/octet-stream".
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    yaga = os.listdir('/Applications/XAMPP/xamppfiles/htdocs/Uploads/')
    filename1 = '/Applications/XAMPP/xamppfiles/htdocs/Uploads/'
    yaga2 = len(yaga) - 1
    filename3 = filename1 + yaga[yaga2]
    print(filename3)
    #filename2 = '/Applications/XAMPP/xamppfiles/htdocs/Uploads/handnotes3.jpg'
    k = open(filename3,'rb')
    body = k.read()
    k.close()


    # The URL of a JPEG image containing handwritten text.
    #body = "{'url':'C:/xampp/htdocs/bigredhax2017/Uploads/handnotes.jpg'}"

    # For printed text, set "handwriting" to false.
    params = urllib.urlencode({'handwriting' : 'true'})

    try:
        # This operation requrires two REST API calls. One to submit the image for processing,
        # the other to retrieve the text found in the image.
        #
        # This executes the first REST API call and gets the response.
        conn = httplib.HTTPSConnection(uri_base)
        conn.request("POST", "/vision/v1.0/RecognizeText?%s" % params, body, headers)
        response = conn.getresponse()

        # Success is indicated by a status of 202.
        if response.status != 202:
            # Display JSON data and exit if the first REST API call was not successful.
            parsed = json.loads(response.read())
            print ("Error:")
            print (json.dumps(parsed, sort_keys=True, indent=2))
            conn.close()
            exit()

        # The 'Operation-Location' in the response contains the URI to retrieve the recognized text.
        operationLocation = response.getheader('Operation-Location')
        parsedLocation = operationLocation.split(uri_base)
        answerURL = parsedLocation[1]

        # NOTE: The response may not be immediately available. Handwriting recognition is an
        # async operation that can take a variable amount of time depending on the length
        # of the text you want to recognize. You may need to wait or retry this GET operation.

        #print('\nHandwritten text submitted. Waiting 10 seconds to retrieve the recognized text.\n')
        time.sleep(10)

        # Execute the second REST API call and get the response.
        conn = httplib.HTTPSConnection(uri_base)
        conn.request("GET", answerURL, '', headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        print ("Response:")
        jsonInput = json.dumps(parsed, sort_keys=True, indent=2)
        conn.close()

    except Exception as e:
        print('Error:')
        print(e)


    ####################################
    # This is something which converts a given JSON-string to a better
    # string for keyword analysis

    def jsonToTxt(jsonString):
        substringListOne=jsonString.split('"text": ')
        substringListTwo=[]
        stronk=""
        for sub in substringListOne:
            sub=sub[1:]
            i=0
            for s in sub:
                if (s=='\"'):
                    break
                i+=1
            sub=sub[:i]
            if len(sub)==0:
                stronk+=sub
            else:
                stronk+=sub+" "
        return stronk

    stank = jsonToTxt(jsonInput)

    ###########
    # This will find the keywords in stank
    from rake_nltk import Rake
    r = Rake()
    a = r.extract_keywords_from_text(stank)
    b = r.get_ranked_phrases()
    print(b[0])
    return b[0]
justDoIt()