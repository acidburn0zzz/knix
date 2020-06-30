# !/usr/bin/python3

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

import sys
import ruamel.yaml

# get the custom values from the build environment set by the user
with open("../../build_env.mk") as fp:
    build_env = fp.read().strip()

build_env = build_env.split("\n")

image_names = {}

PREFIX_TEXT = "KUBERNETES_CUSTOM_PREFIX"

# 1. find the Kubernetes custom prefix to be applied to image names
for line in build_env:
    if not line.startswith("#"):
        prefix_index = line.find(PREFIX_TEXT)
        if prefix_index == 0:
            prefix = line.split("=")[1].strip()
            break

# 2. find the image name keys
for line in build_env:
    if not line.startswith("#"):
        prefix_index = line.find(PREFIX_TEXT)
        if prefix_index != 0 and prefix_index != -1:
            tokens = line.split("=")
            key = tokens[0].strip()
            value = tokens[1].strip()
            value = value.replace("$(" + PREFIX_TEXT + ")", prefix)
            image_names[key] = value

#print(image_names)

# obtain the original values.yaml
yaml = ruamel.yaml.YAML()

with open("../../deploy/helm/microfunctions/values.yaml") as fp:
    data = yaml.load(fp)

# modify the obtained values.yaml file with the custom values obtained above
for param in data:
    image_key = param.upper() + "_IMAGE_NAME"
    if image_key in image_names:
        if param == "manager":
            data[param]["setup"]["imagePath"] = "/" + image_names[image_key]
            sandbox_data = data[param]["sandbox"]
            sandbox_data["imagePathPython"] = "/" + image_names["SANDBOX_IMAGE_NAME"]
            sandbox_data["imagePathJava"] = "/" + image_names["SANDBOX_JAVA_IMAGE_NAME"]
            #for key in sandbox_data:
            #    print(key + "->" + str(sandbox_data[key]))
        elif param == "nginx":
            data[param]["imagePath"] = "/" + image_names[image_key]
        elif param == "datalayer":
            data[param]["imagePath"] = "/" + image_names[image_key]
        elif param == "riak":
            data[param]["imagePath"] = "/" + image_names[image_key]
        print(data[param])

prefix = prefix.replace("/", "")
if prefix != "":
    # write the custom values.yaml
    with open("../../deploy/helm/microfunctions/" + prefix + "values.yaml", "w") as f:
        yaml.dump(data, f)
