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

def handle(event, context):
    import tensorflow as tf
    # Simple hello world using TensorFlow
    c = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    Shape = c.get_shape().as_list()
    print(Shape)   # [2,3]


    #x = [[2.]]
    #print('tensorflow version', tf.__version__)
    #print('hello, {}'.format(tf.matmul(x, x)))
    #y = tf.matmul(x, x)
    #print('result, {}'.format(y)
    #return json.dumps(tf.matmul(x, x)) 
    return "Done"
    #return str(tf.matmul(x, x).get_shape())
