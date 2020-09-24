import datetime
import os
import sys
import time

from typing import Optional
from fastapi import FastAPI, Response, status, File, UploadFile, Form
import uvicorn

#from src.controllers.image_processor import ImageProcessor
from src.controllers.image_controller import ImageController

OCR_SERVING_HOST = '0.0.0.0:8500'
# Setup application
app = FastAPI()

# return JSON
ret = dict()

@app.get('/')
async def health_check(response: Response):
    response.headers["Hostname"] = "hostname"
    response.headers["X-FPTAI-BILLING"] = '0'
    return {'success': True}

# @app.post('/detect')
# async def read_api(response: Response, 
#                    image: Optional[UploadFile] = File(None),
#                    image_url: Optional[str] = Form(None)):
#     print('Started new at: ' + str(datetime.datetime.now()))
#     response.status_code = status.HTTP_200_OK
#     response.headers["X-FPTAI-BILLING"] = '1'
#     result = dict()
#     img_processor = ImageProcessor(DETECT_SERVING_HOST)

#     if image is not None:
#         image = image.file.read()
#         result = img_processor.fruit_detect(image)
#         print(result)
#     return result

# @app.post('/classify')
# async def read_api(response: Response, 
#                    image: Optional[UploadFile] = File(None),
#                    image_url: Optional[str] = Form(None)):
#     print('Started new at: ' + str(datetime.datetime.now()))
#     response.status_code = status.HTTP_200_OK
#     response.headers["X-FPTAI-BILLING"] = '1'
#     result = dict()
#     img_processor = ImageProcessor(CLASSIFY_SERVING_HOST)

#     if image is not None:
#         image = image.file.read()
#         result = img_processor.fruit_classify(image)
#         print(result)
#     return result

@app.post('/OCR')
async def read_api(response: Response, 
                   image: Optional[UploadFile] = File(None),
                   image_url: Optional[str] = Form(None)):
    print('Started new at: ' + str(datetime.datetime.now()))
    response.status_code = status.HTTP_200_OK
    response.headers["X-FPTAI-BILLING"] = '1'
    result = dict()

    img_controller = ImageController()

    try:
        print('0')
        print(image)
        print(image_url)
        if image is not None:
            data_type = 'image'
            result = img_controller.process_image(image, data_type, "detect")
            print(result['data'])
        elif image_url is not None:
            data_type = 'url'
            result = img_controller.process_image(image, data_type, "detect")
            print(result)
        else:
            result['error'] = 'Invalid Parameters or Values!'

        if 'error' in result:
            response.headers["X-FPTAI-BILLING"] = '0'
            response.status_code = status.HTTP_400_BAD_REQUEST
            if result['error'] == 'Invalid Parameters or Values!':
                ret['errorCode'] = 1
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Please upload only 2 images in the list':
                ret['errorCode'] = 2
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Unable to find ID card in the image':
                ret['errorCode'] = 3
                ret['errorMessage'] = result['error']
                ret['data'] = []
                response.headers["X-FPTAI-BILLING"] = '1'
            elif result['error'] == 'Downloading file timed out':
                ret['errorCode'] = 4
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'No URL in the request':
                ret['errorCode'] = 5
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Failed to open the URL!':
                ret['errorCode'] = 6
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Invalid image file':
                ret['errorCode'] = 7
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Bad data':
                ret['errorCode'] = 8
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'No string base64 in the request':
                ret['errorCode'] = 9
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'String base64 is not valid':
                ret['errorCode'] = 10
                ret['errorMessage'] = result['error']
                ret['data'] = []
            else:
                ret['errorCode'] = 1
                ret['errorMessage'] = 'Invalid Parameters or Values!'
                ret['data'] = []
        else:
            ret['errorCode'] = 0
            ret['errorMessage'] = ''
            ret['data'] = result['data']
               
        return ret
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'error': 'Something wrong has happened'}

@app.post('/classify')
async def read_api(response: Response, 
                   image: Optional[UploadFile] = File(None),
                   image_url: Optional[str] = Form(None)):
    print('Started new at: ' + str(datetime.datetime.now()))
    response.status_code = status.HTTP_200_OK
    response.headers["X-FPTAI-BILLING"] = '1'
    result = dict()

    img_controller = ImageController(CLASSIFY_SERVING_HOST)

    try:
        # print('0')
        # print(image)
        # print(image_url)
        if image is not None:
            data_type = 'image'
            result = img_controller.process_image(image, data_type, "classify")
        
        elif image_url is not None:
            data_type = 'url'
            result = img_controller.process_image(image, data_type, "classify")
        else:
            result['error'] = 'Invalid Parameters or Values!'

        if 'error' in result:
            response.headers["X-FPTAI-BILLING"] = '0'
            response.status_code = status.HTTP_400_BAD_REQUEST
            if result['error'] == 'Invalid Parameters or Values!':
                ret['errorCode'] = 1
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Please upload only 2 images in the list':
                ret['errorCode'] = 2
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Unable to find ID card in the image':
                ret['errorCode'] = 3
                ret['errorMessage'] = result['error']
                ret['data'] = []
                response.headers["X-FPTAI-BILLING"] = '1'
            elif result['error'] == 'Downloading file timed out':
                ret['errorCode'] = 4
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'No URL in the request':
                ret['errorCode'] = 5
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Failed to open the URL!':
                ret['errorCode'] = 6
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Invalid image file':
                ret['errorCode'] = 7
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'Bad data':
                ret['errorCode'] = 8
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'No string base64 in the request':
                ret['errorCode'] = 9
                ret['errorMessage'] = result['error']
                ret['data'] = []
            elif result['error'] == 'String base64 is not valid':
                ret['errorCode'] = 10
                ret['errorMessage'] = result['error']
                ret['data'] = []
            else:
                ret['errorCode'] = 1
                ret['errorMessage'] = 'Invalid Parameters or Values!'
                ret['data'] = []
            
        else:
            ret['errorCode'] = 0
            ret['errorMessage'] = ''
            ret['data'] = result['data']
               
        return ret
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'error': 'Something wrong has happened'}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8888, log_level="info", reload=True)
