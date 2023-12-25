def rref(A):
    n = len(A)
    m = len(A[0])
    l = 0
    for r in range(n):
        if l >= m:
            return A
        i = r
        while A[i][l] == 0:
            i += 1
            if i == n:
                i = r
                l += 1
                if l == m:
                    return A
        A[i], A[r] = A[r], A[i]
        lv = A[r][l]
        A[r] = [x / lv for x in A[r]]
        for i in range(n):
            if i != r:
                lv = A[i][l]
                A[i] = [A[i][j] - lv * A[r][j] for j in range(m)]
        l += 1
    return A
        
def dict_val(rref_mt):
    col = len(rref_mt[0])
    rows = len(rref_mt)
    d_var={}
    for i in range(col):
        var_name="X"+str(i)
        d_var[var_name]="free"
    list_eq=[0]*col
    for i in range(rows):
        if 1 in  rref_mt[i]:
            p_index=rref_mt[i].index(1)
        Flag=True
        for j in range (col):
            if j!=p_index and rref_mt[i][j]!=0:
                list_eq[j]=rref_mt[i][j]
                Flag=False
        if Flag==False:
            var_name="X"+str(p_index)
            d_var[var_name]=list_eq
            list_eq=[0]*col
        elif 1 in rref_mt[i]:
            var_name="X"+str(p_index)
            d_var[var_name]=0
    return d_var
def simp_dic(dict_main):
    list_key=[]
    list_eq=[]
    for x in dict_main.keys():
        if dict_main[x] == 0:
            list_key.append(x)
        elif type(dict_main[x]) is list:
            list_eq.append(x)
    
    for key in list_key:
        for list_com in list_eq:
            temp_val=int(key[1:])
            dict_main[list_com][temp_val]=0
    
    return dict_main
def para_eq(modify_dict,rref):
    list_const=[]
    list_eq=[]
    list_free=[]
    list_keys=[f"X{col}" for col in range(len(rref[0]))]
    print(list_keys,end="")
    print("=",end="")
    for key in modify_dict.keys():
        if type(modify_dict[key]) is str:
            list_free.append(key[1:])
        elif modify_dict[key] == 0:
            list_const.append(key[1:])
        else:
            list_eq.append(key[1:])

    list1=[0]
    list2=list1*len(rref[0])
    
    Flag=False
    for i in list_free:
        if Flag==True:
            print("+ ",end="")
        for k,val in modify_dict.items():
            if type(val) is list:
                a=int(k[1:])
                b=int(i)
                list2[a]=-(val[b])
            elif(type(val) is str):
                c=int(k[1:])
                if(c==int(i)):
                    list2[c]=1
        print(list2,end="")
        print(f"X{i} ",end="")
        Flag=True
        list1=[0]
        list2=list1*len(rref[0])

    if len(list_free)==0:
        print(list2)
# matrix_input =  [[4,4,4],[2,2,2],[1,1,1]]
# matrix_input =  [[1,-2,-1,3,0],[-2,4,5,-5,3],[3,-6,-6,8,2]]
# matrix_input =  [[1,-1,-1,3],[1,1,-2,1],[4,-2,4,1]]
# matrix_input =  [[3,5,-4],[-3,-2,4],[6,1,-8]]
# matrix_input =  [[1,0,0],[0,2,0],[0,1,3]]

f=open("matrix_input.txt","r")
a=f.readline().split(":")
m=int(a[1])
b=f.readline().split(":")
n=int(b[1])
matrix_input=list()
for i in range (m):
    x=list(map(int,f.readline().split()))
    matrix_input.append(x)
rref_=rref(matrix_input)
print(rref_)
dict_main=dict_val(rref_)
modify_dict=simp_dic(dict_main)
print(modify_dict)
para_eq(modify_dict,rref_)
f.close()
