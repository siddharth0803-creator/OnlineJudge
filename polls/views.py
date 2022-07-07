from django.shortcuts import render
from django.http import HttpResponse
from .models import Problems, Test, Solutions
import os, sys, subprocess
# Create your views here.
def index(request):
    problem_list=Problems.objects.all()
    context={
        'problem_list':problem_list
    }
    return render(request,'Home.html',context)


def Description(request, problem_id):
    pro = Problems.objects.get(id=problem_id)
    io=Test.objects.filter(problem=pro)[0]
    codearea=""
    original_stdout=""
    output=""
    y=""
    if request.method=="POST":
        codearea=request.POST['codearea']
        input_part = request.POST['input']
        input=bytes(input_part, 'utf-8')
        y = input_part
        #input_part = input_part.replace("\n"," ").split(" ")
        #def input():
            #a = input_part[0]
            #del input_part[0]
            #return a
        try:
            cpp=open('code.cpp','w')
            cpp.write(codearea)
            cpp.close()
            subprocess.run(['g++','code.cpp','-o','a.exe'])
            out = subprocess.run(['a.exe'], capture_output=True, input = input, timeout=1)
            output = out.stdout.decode("utf-8")
            #out=subprocess.run(['g++','-o','a.exe','code.cpp'], capture_output=True, input=input_part,shell=True, text=True, check=True, timeout=1)
            if(out.returncode!=0):
                    print('comp err')
                    return HttpResponse('comp err')
            #subprocess.call("dir",shell=True)
        except Exception as e:
            output=e
    context={
        'input': y,
        "problem_id":problem_id,
        "code":codearea,
        'problem':pro,
        'io':io,
        'output':output,
    }
    pro.code=codearea
    pro.save()
    return render(request,'Description.html',context)


def Result(request, problem_id):
    pro=Solutions.objects.filter(id=problem_id)
    p = Problems.objects.get(id=problem_id)
    io=Test.objects.filter(problem=problem_id)
    codearea=""
    original_stdout=""
    output=""
    y=""
    output_list=[]
    test_output=[]
    codearea=p.code
    verdict="true"
    for value in io:
        input_part = value.input
        input=bytes(input_part, 'utf-8')
        y = input_part
        #input_part = input_part.replace("\n"," ").split(" ")
        #def input():
            #a = input_part[0]
            #del input_part[0]
            #return a
        try:
            subprocess.run(['g++','code.cpp','-o','a.exe'])
            out = subprocess.run(['a.exe'], capture_output=True, input = input, timeout=1)
            output = out.stdout.decode("utf-8").split(" ")
            #out=subprocess.run(['g++','-o','a.exe','code.cpp'], capture_output=True, input=input_part,shell=True, text=True, check=True, timeout=1)
            if(out.returncode!=0):
                    print('comp err')
                    return HttpResponse('comp err')
        except Exception as e:
            output=e
        output_list.append(output)


    for p in io:
        test_output.append(p.output.replace("\n"," ").split(" "))

    for i in range(0, len(test_output)):
            if output_list[i][0] != test_output[i][0] :
                verdict="false"
                break
    if(verdict=="true"):
        verdict="Right"
        color="success"
    else:
        verdict="Wrong"
        color="danger"
    context={
        'verdict':verdict,
        'color':color,
        'output_list':output_list,
        'test_output':test_output
    }
    return render(request,'verdict.html',context)

''''
def Description(request, problem_id):
    pro = Problems.objects.get(id=problem_id)
    io=Test.objects.filter(problem=pro)[0]
    codearea=""
    original_stdout=""
    output=""
    y=""
    if request.method=="POST":
        codearea=request.POST['codearea']
        input_part = request.POST['input']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt','w')
            exec(codearea)
            sys.stdout.close()
            sys.stdout =original_stdout

            output= open('file.txt','r').read()

        except Exception as e:
            sys.stdout= original_stdout
            output=e
    context={
        'input': y,
        "problem_id":problem_id,
        "code":codearea,
        'problem':pro,
        'io':io,
        'output':output,
    }
    pro.code=codearea
    pro.save()
    return render(request,'Description.html',context)
'''

'''
def Result(request, problem_id):
    pro=Solutions.objects.filter(id=problem_id)
    p = Problems.objects.get(id=problem_id)
    io=Test.objects.filter(problem=problem_id)
    codearea=""
    original_stdout=""
    output=""
    y=""
    output_list=[]
    test_output=[]
    codearea=p.code
    verdict="true"
    for value in io:
        input_part = value.input
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt','w')
            exec(codearea)
            sys.stdout.close()
            sys.stdout =original_stdout

            output= open('file.txt','r').read()
            output_list.append(output.splitlines())
        except Exception as e:
            sys.stdout= original_stdout
            output=e
    for p in io:
        test_output.append(p.output.replace("\n"," ").split(" "))

    for i in range(0, len(test_output)):
            if output_list[i][0] != test_output[i][0] :
                verdict="false"
                break
    if(verdict=="true"):
        verdict="Right"
        color="success"
    else:
        verdict="Wrong"
        color="danger"
    context={
        'verdict':verdict,
        'color':color,
        'output_list':output_list,
        'test_output':test_output
    }
    return render(request,'verdict.html',context)
'''
