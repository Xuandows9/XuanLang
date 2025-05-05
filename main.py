import sys,os,string
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Code:
    def __init__(self,codestring):
        self.codestring=codestring
        try:
            self.args=codestring.split("(")[1][0:-1]
            self.func=codestring.split("(")[0]
            self.run()
        except:
            print(f" {bcolors.FAIL}{bcolors.BOLD}语法错误!{bcolors.ENDC}\n   {bcolors.BOLD}文件:{bcolors.ENDC}{bcolors.OKBLUE}\"{filename}\"{bcolors.ENDC}\n     {bcolors.BOLD}代码：{bcolors.WARNING}\"{self.codestring}\"{bcolors.ENDC}\n            {bcolors.FAIL}{'^'*len(self.codestring)}{bcolors.ENDC}")
            exit()
    def  run(self):
        print(f"{'正在运行  代码：'+self.codestring+'，方法：'+self.func+'，参数：'+self.args}")

        
def main():
    try:
        f=open(filename,"r")
    except:
        print(f" {bcolors.FAIL}{bcolors.BOLD}IO错误!{bcolors.ENDC}\n  找不到文件：{bcolors.OKBLUE}\"{filename}\"{bcolors.ENDC}")
        exit()
    codes=[]
    codes=f.read()
    codes=codes.replace("\n","")
    temp=[]
    temp_a=False
    for char in codes:
        if char=="\"":
            temp_a=not temp_a
        elif temp_a:
            temp.append(char)
        elif char not in string.whitespace:
            temp.append(char)
    codes="".join(temp)      
            
    codes=codes.split(";")
    codes=codes[0:-1] if codes[-1]=="" else codes
    for code in codes:
        Code(code)




if __name__ =="__main__":
    args=sys.argv
    for i in range(len(args)):
        if args[i]=="-f":
            filename=args[i+1]

    main()
