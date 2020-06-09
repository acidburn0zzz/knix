#   Copyright 2020 The KNIX Authors

#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#import json 

#import os
#content = ""

#try:
#    curdir = os.path.dirname(__file__)
#    print("function's current directory: " + curdir)

def handle(event, context):
    import os
    curdir = os.path.dirname(__file__)

    # Simple hello world using Face_Recognition
    import face_recognition
    image = face_recognition.load_image_file("/opt/mfn/workflow/states/tensorf/facer/obama.jpg")
    face_locations = face_recognition.face_locations(image)    
    return str(face_locations)#str(face_recognition.__version__)
    #return "Hello Face!"

