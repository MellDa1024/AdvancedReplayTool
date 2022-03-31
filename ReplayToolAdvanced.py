#ReplayToolAdvanced.py
#Made By MellDa
#YuDecompiledThis?
#Hello
import os
import sys
import time
import json
def returnthepath(relative_path):
    return os.path.join(os.path.abspath(""),relative_path)
def chunklist(list_,len_):
    return [list_[i:i+len_] for i in range(0, len(list_), len_)]
def filterlist(list_):
    temp=[]
    for i in list_:
        if i[-5:] =='.rofl':
            temp.append(i)
    return temp
def checkjson():
    if 'ReplayToolData.json' in os.listdir(os.path.abspath("")):
        path=returnthepath("ReplayToolData.json")
        with open(path, 'r', encoding='UTF8') as f:
            try:
                json_data = json.load(f, encoding='UTF8')
            except:
                return False
        if json_data['RoflDir'].strip(" ") != "" and json_data['LoLDir'].strip(" ") != "":
            return True
        else:
            return False
    else:
        return False
def nojsonfile():
    os.system('cls')
    title()
    sys.stdout.write("\n")
    menubar()
    sys.stdout.write("\n 정보를 저장하는 ReplayToolData.json을 불러 올 수 없거나 파일이 손상되었습니다.\n")
    sys.stdout.write(" ReplayToolData.json가 본 프로그램과 같은 폴더 내에 있는지 확인해주세요.\n\n")
    sys.stdout.write(" 본 프로그램을 처음 실행하거나 ReplayToolData.json를 다시 생성하시는 경우,\n 메뉴에서 3번을 입력해주세요.\n\n")
    sys.stdout.flush()
    input(" 엔터를 눌러 메뉴로 돌아가세요.")
def main():
    title()
    sys.stdout.write(" └─ Made By MellDa / Version : Beta-1.0.3(Bootloader Fixed) ─┘\n\n ┌──────── Contact ────────┐\n │ Discord : MellDa#0001   │\n │ meltdown1024@naver.com  │\n └─────────────────────────┘\n")
    sys.stdout.flush()
    input("\n Press Enter to continue... ")
    while True:
        chosen=choose()
        if chosen==1:
            if checkjson():
                makeareplay()
            else:
                nojsonfile()
        elif chosen==2:
            if checkjson():
                recentreplay()
            else:
                nojsonfile()
        elif chosen==3:
            changearoot()
        elif chosen==4:
            sys.exit()
def title():
    os.system('cls')
    sys.stdout.write("     ____                __              ______               __\n")
    sys.stdout.write("    / __ \ ___   ____   / /____ _ __  __/_  __/____   ____   / /\n")
    sys.stdout.write("   / /_/ // _ \ / __ \ / // __ `// / / / / /  / __ \ / __ \ / / \n")
    sys.stdout.write("  / _, _//  __// /_/ // // /_/ // /_/ / / /  / /_/ // /_/ // /  \n")
    sys.stdout.write(" /_/ |_| \___// .___//_/ \__,_/ \__, / /_/   \____/ \____//_/   \n")
    sys.stdout.write("     ___     /_/__             /____/                   __      \n")
    sys.stdout.write("    /   |  ____/ /_   __ ____ _ ____   _____ ___   ____/ /      \n")
    sys.stdout.write("   / /| | / __  /| | / // __ `// __ \ / ___// _ \ / __  /       \n")
    sys.stdout.write("  / ___ |/ /_/ / | |/ // /_/ // / / // /__ /  __// /_/ /        \n")
    sys.stdout.write(" /_/  |_|\__,_/  |___/ \__,_//_/ /_/ \___/ \___/ \__,_/         \n\n")
    sys.stdout.flush()
def menubar():
    sys.stdout.write(" ┌───┬──────────────────────────────┐\n")
    sys.stdout.write(" │ 1 │  Rofl 파일 열기              │ \n")
    sys.stdout.write(" ├───┼──────────────────────────────┤\n")
    sys.stdout.write(" │ 2 │  최근 실행한 Rofl 파일 열기  │ \n")
    sys.stdout.write(" ├───┼──────────────────────────────┤\n")
    sys.stdout.write(" │ 3 │  Rofl / 롤 폴더 위치 설정    │ \n")
    sys.stdout.write(" ├───┼──────────────────────────────┤\n")
    sys.stdout.write(" │ 4 │  나가기                      │ \n")
    sys.stdout.write(" └───┴──────────────────────────────┘\n")
    sys.stdout.flush()
def roflbar(list_, len_,cnt,maxcnt):
    if len_ < 25:
        len_=25
    print(" ┌"+"선택".center(len_+5, "─")+"┐")
    for i in range(len(list_)):
        msg="{0}. ".format(i+1)+list_[i]
        print(" │ "+msg.ljust(len_+6," ")+"│")
    print(" └"+"({0}/{1})".format(cnt,maxcnt).center(len_+7, "─")+"┘")
def choose():
    os.system('cls')
    title()
    sys.stdout.write("\n")
    menubar()
    a = input("\n 입력 : ")
    while True:
        if a == "1" or a == "2" or a == "3" or a == "4":
            return int(a)
        else:
            a = input("\033[F\033[K 잘못된 번호입니다, 다시 입력해주세요 : ")
def makeareplay():
    title()
    sys.stdout.write("\n")
    sys.stdout.flush()
    path=returnthepath("ReplayToolData.json")
    with open(path, 'r', encoding='UTF8') as f:
        json_data = json.load(f, encoding='UTF8')
    for i in range(1,4):
        if i==3:
            rofldir=json_data['RoflDir']
        else:
            rofldir="Finding..."
        msg="\r\033[K Rofl 파일을 불러오는 중{0} / 경로 : {1}".format("."*i, rofldir)
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n")
    sys.stdout.flush()
    fileexists=True
    for i in range(1,4):
        if i==3:
            loldir=json_data['LoLDir']
        else:   
            loldir="Finding..."
        msg="\r\033[K 리그 오브 레전드의 경로를 불러오는 중{0} / 경로 : {1} ".format("."*i, loldir)
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.5)
    rofldir=rofldir.strip()
    loldir=loldir.strip()
    try:
        if "League of Legends.exe" not in os.listdir(os.path.join(loldir,"Game")):
            sys.stdout.write("\n 리그 오브 레전드 프로그램이 지정된 폴더에 존재하지 않아 Rofl 파일을 열 수 없습니다.")
            sys.stdout.flush()
            fileexists=False
            input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
    except:
        sys.stdout.write("\n 리그 오브 레전드 폴더가 존재하지 않아 Rofl 파일을 열 수 없습니다.")
        sys.stdout.flush()
        fileexists=False
        input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
    if fileexists:
        try:
            rofllist=chunklist(filterlist(os.listdir(rofldir)),10)
            if rofllist == []:
                sys.stdout.write("\n Rofl 파일을 찾을 수 없습니다. Rofl가 있는 폴더를 확인해 주세요.")
                fileexists=False
                sys.stdout.flush()
                input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
        except:
            sys.stdout.write("\n Rofl 파일이 저장된 폴더가 존재하지 않아 Rofl 파일을 열 수 없습니다.")
            sys.stdout.flush()
            fileexists=False
            input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
    if fileexists:
        sys.stdout.write("\n\n 완료!\n")
        sys.stdout.flush()
        input(" 리그 오브 레전드와 Rofl 파일의 경로를 확인해주시고 엔터를 눌러주세요.")
        page=0
        while True:
            os.system('cls')
            sys.stdout.write(" Rofl 파일 경로 : {0}\n\n".format(rofldir))
            sys.stdout.flush()
            checklen=len(sorted(rofllist[page], key=lambda x: -len(x))[0])
            maxcnt=len(rofllist)
            roflbar(rofllist[page],checklen,page+1,maxcnt)
            sys.stdout.write(" B : 이전 페이지 / N : 다음 페이지\n X : 나가기\n\n")
            sys.stdout.flush()
            getreact=input(" 입력 : ")
            while True:
                if getreact.strip("0123456789NBXnbx ") != "": #번호, N B X 이외 다른 string
                    getreact = input("\033[F\033[K 다시 입력해주세요 : ")
                elif getreact=="": #빈칸인 경우
                    getreact = input("\033[F\033[K 다시 입력해주세요 : ")
                elif getreact.find('N') != -1 or getreact.find('B') != -1 or getreact.find('X') != -1 or getreact.find('n') != -1 or getreact.find('b') != -1 or getreact.find('x') != -1:
                    #단독 N나 B 또는 X가 아닐 경우
                    if len(getreact.strip(" ")) != 1:
                        getreact = input("\033[F\033[K 다시 입력해주세요 : ")
                    else:
                        break
                elif getreact.find('N') == -1 and getreact.find('B') == -1 and getreact.find('X') == -1 and getreact.find('n') == -1 and getreact.find('b') == -1 and getreact.find('x') == -1:
                    #숫자이면서
                    if int(getreact.strip(" "))>10 or int(getreact.strip(" "))<1: #N<1 or N>10인 경우
                        getreact = input("\033[F\033[K 범위 내의 숫자가 아닙니다. 다시 입력해주세요 : ")
                    else:
                        break
                else:
                    break
            getreact=getreact.strip(" ")
            if getreact == "N" or getreact == "n":
                if page!=maxcnt-1:
                    page+=1
            elif getreact == "B" or getreact == "b":
                if page!=0:
                    page-=1
            elif getreact == "X" or getreact == "x":
                break
            else:
                while True:
                    finalcheck = input("\033[F\033[K 파일명 '{0}'를 실행시키겠습니까? (Y/N) : ".format(rofllist[page][int(getreact)-1]))
                    if finalcheck == "Y" or finalcheck == "y":
                        jsondict={"RoflDir": rofldir,
                                "LoLDir": loldir,
                                "IsQueued": True,
                                "QueuedRoflDir": rofldir,
                                "QueuedRoflName": rofllist[page][int(getreact)-1],
                                "QueuedLoLDir": loldir}
                        openreplay(rofllist[page][int(getreact)-1], rofldir, loldir, jsondict)
                        break
                    elif finalcheck == "N" or finalcheck == "n":
                        break
def recentreplay():
    title()
    path=returnthepath("ReplayToolData.json")
    with open(path, 'r', encoding='UTF8') as f:
        json_data = json.load(f, encoding='UTF8')
    isqueued = json_data['IsQueued']
    if isqueued:
        RoflDir=json_data['QueuedRoflDir']
        RoflName=json_data['QueuedRoflName']
        LoLDir=json_data['QueuedLoLDir']
        sys.stdout.write("\n 파일명 '{0}'를 실행시키겠습니까?\n 리그 오브 레전드 경로 : {1}\n\n".format(RoflName, LoLDir))
        sys.stdout.flush()
        while True:
            finalcheck = input("\033[F\033[K 입력(Y/N) : ")
            finalcheck
            if finalcheck == "Y" or finalcheck == "y":
                try:
                    if "League of Legends.exe" not in os.listdir(os.path.join(LoLDir,"Game")):
                        sys.stdout.write("\n 리그 오브 레전드 프로그램이 지정된 폴더에 존재하지 않아 Rofl 파일을 열 수 없습니다.")
                        sys.stdout.flush()
                        input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
                        break
                except:
                    sys.stdout.write("\n 리그 오브 레전드 폴더가 존재하지 않아 Rofl 파일을 열 수 없습니다.")
                    sys.stdout.flush()
                    input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
                    break
                try:
                    if RoflName not in os.listdir(RoflDir):
                        sys.stdout.write("\n '{0}'가 지정된 폴더에 존재하지 않아 Rofl 파일을 열 수 없습니다.".format(RoflName))
                        sys.stdout.flush()
                        input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
                        break
                except:
                    sys.stdout.write("\n 리플레이 파일이 있었던 폴더가 존재하지 않아 Rofl 파일을 열 수 없습니다.")
                    sys.stdout.flush()
                    input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
                    break
                openreplay(RoflName, RoflDir, LoLDir, False)
                break
            elif finalcheck == "N" or finalcheck == "n":
                break
    else:
        sys.stdout.write("\n 최근 실행된 Rofl 파일이 없습니다.")
        sys.stdout.flush()
        input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
def openreplay(rofl, rofldir, loldir, jsondict):
    sys.stdout.write(" \n\n")
    for i in range(1,4):
        msg="\r\033[K 실행중입니다{0}".format("."*i)
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.5)
    path=returnthepath("ReplayToolData.json")
    homepath=os.path.abspath("")
    if jsondict != False:
        with open(path, 'w', encoding='UTF8') as f:
            json.dump(jsondict, f, ensure_ascii = False, sort_keys=True, indent=4)
    game = loldir + '\\Game'
    rofl=os.path.join(rofldir,rofl)
    os.chdir('{0}'.format(game))
    sending = '""League of Legends.exe" "{0}" -GameBaseDir={1} -Locale=ko_KR -SkipBuild -EnableLNP -UseNewX3D=1 -UseNewX3DFramebuffers=1"'.format(rofl, game)
    os.system(sending)
    os.chdir(homepath)
def changearoot():
    title()
    sys.stdout.write("\n")
    sys.stdout.flush()
    IsQueued = False
    QueuedRoflDir = ""
    QueuedRoflName = ""
    QueuedLoLDir = ""
    if 'ReplayToolData.json' not in os.listdir(os.path.abspath("")):
        sys.stdout.write(" ReplayToolData.json가 같은 폴더 내에 존재하지 않습니다, ReplayToolData.json 파일을 생성합니다.\n")
        sys.stdout.flush()
    else:
        path=returnthepath("ReplayToolData.json")
        with open(path, 'r', encoding='UTF8') as f:
            try:
                json_data = json.load(f, encoding='UTF8')
                IsQueued=json_data['IsQueued']
                QueuedRoflDir=json_data['QueuedRoflDir']
                QueuedRoflName=json_data['QueuedRoflName']
                QueuedLoLDir=json_data['QueuedLoLDir']
            except:
                IsQueued = False
                QueuedRoflDir = ""
                QueuedRoflName = ""
                QueuedLoLDir = ""
    rofldir=input(" 실행할 리플레이 파일이 있는 경로를 입력해주세요.\n 예시 : C:\\USER\\문서\\League of Legends\\Replays\n 입력 : ").strip(" ")
    loldir=input("\n 사용할 리그 오브 레전드 파일이 있는 경로를 입력해주세요.\n 예시 : C:\\Riot Games\\League of Legends\n 입력 : ").strip(" ")
    jsondict={"RoflDir": rofldir,
            "LoLDir": loldir,
            "IsQueued": IsQueued,
            "QueuedRoflDir": QueuedRoflDir,
            "QueuedRoflName": QueuedRoflName,
            "QueuedLoLDir": QueuedLoLDir}
    sys.stdout.write("\n\n")
    for i in range(1,4):
        msg="\r\033[K Json 파일을 생성중입니다{0}".format("."*i)
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.5)
    path=returnthepath("ReplayToolData.json")
    with open(path, 'w', encoding='UTF8') as f:
        json.dump(jsondict, f, ensure_ascii = False, sort_keys=True, indent=4)
    sys.stdout.write("\r\033[K 생성되었습니다!")
    sys.stdout.flush()
    input("\n\n 엔터를 눌러 메뉴로 돌아가세요.")
if __name__ == "__main__":
    main()