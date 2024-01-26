from os import walk,path,mkdir,listdir,remove,rmdir
from pandas import read_csv, DataFrame
from numpy import array, arange, log, sqrt,meshgrid, rot90,linspace,sort
from scipy import interpolate
from scipy.signal import savgol_filter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
import ipywidgets as widgets
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from urllib.request import urlopen
import warnings
warnings.filterwarnings('ignore')
print('Software de visualizacao de arquivos de STS Nanosurf v1.3.2. Arquivos tipo csv (x,y,z) ')
print('By Rafael Reis Barreto, contato rafinhareis17@gmail.com')
print('Se sentir no fundo do coracaozinho, poe meu nome no artigo =D')


def load_file(path):
    df = read_csv ( path, sep= ';', names= ['x','y','z'])
    first_value = df[df.columns[0]].iloc[0] 
    V = []
    for i in range(1,len(df)):
        if df[df.columns[0]].iloc[i]  == first_value:
            count = i
            #V.append(df[df.columns[0]].iloc[i])
            break
        else:
            V.append(df[df.columns[0]].iloc[i])

    n = int(len(df)/count)



    dataframes = []
    names = []
    Vmin = min(V)
    Vmax = max(V)
    for j in range(n):
        sts=[]
        volta =[]

        for i in range(len(df)):
            if i<count :
                filtro_alto = 18*pow(10,-9)
                filtro_baixo = -filtro_alto
                voltagem = df[df.columns[0]].iloc[i]
                corrente = df[df.columns[2]].iloc[i+j*count]
                if corrente>filtro_baixo and corrente < filtro_alto:
                    volta.append(voltagem)
                    sts.append(corrente)
                else:
                    pass
            else:
                break

        V_new = volta
        try:
            
            if min(V_new)>Vmin:
                Vmin = min(V_new)
            if max(V_new)<Vmax:
                Vmax = max(V_new)
            df_new = DataFrame(V_new,columns = ['V'])
            df_new['I'+str(j)] = sts
            names.append(str(j) )
            dataframes.append(df_new)
        except ValueError:
            print('File %s with bad data.'%path)

    return [dataframes,names,[Vmin,Vmax]]


def open_files():
    global folder
    global filenames
    global files_data
    global conca
    gui = Tk()
    gui.geometry("900x900")
    gui.title('Nanosurf STS Data Analise by Rafael Reis Barreto')
    url = "https://i.postimg.cc/2jhtLFy1/teste.png"
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    # In order to display the image in a GUI, you will use the 'PhotoImage' method of Tkinter. It will an image from the directory (specified path) and store the image in a variable.
    #icon = PhotoImage(file = "teste.png")
    icon = PhotoImage(data=raw_data)

    # Finally, to display the image you will make use of the 'Label' method and pass the 'image' variriable as a parameter and use the pack() method to display inside the GUI.
    label = Label(gui, image = icon)
    label.grid(row=0)


    def getFolderPath():
                filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
        )

                global folder
                folder = filedialog.askopenfilename(filetypes=filetypes)
                print("File: ",folder)
                print("Uploaded")
                showinfo(
                title='Selected File',
                message=folder
            )
                
                gui.destroy()



    btnFind = ttk.Button(gui, text="Open File (Single File)", command=getFolderPath)
    btnFind.grid(row=1)

    def select_files():
        global filenames
        global conca
        filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
        )
        conca = False
        filenames = filedialog.askopenfilenames(
            title='Open files (Average)',
            #initialdir='/.',
            filetypes=filetypes)
        print("Files: ")
        for names in filenames:
            print(names)
        print("Uploaded")
        showinfo(
            title='Selected Files',
            message=filenames
        )
        gui.destroy()

    # open button
    open_button = ttk.Button(
        gui,
        text='Open files (Average)',
        command=select_files
    )

    #open_button.pack(expand=True)
    open_button.grid(row=2)

    def select_files2():
        global filenames
        global conca
        filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
        )
        conca = True
        filenames = filedialog.askopenfilenames(
            title='Open files (Concatenate)',
            #initialdir='/.',
            filetypes=filetypes)
        print("Files: ")
        for names in filenames:
            print(names)
        print("Uploaded")
        showinfo(
            title='Selected Files',
            message=filenames
        )
        gui.destroy()

    # open button
    open_button2 = ttk.Button(
        gui,
        text='Open files (Concatenate)',
        command=select_files2
    )

    #open_button.pack(expand=True)
    open_button2.grid(row=3)

    gui.mainloop()



    if filenames!=None:
        files_mult = []
        for item in filenames:
            files_mult.append(load_file(item))
        
        for indice in range(len(filenames[0])):
            ct = len(filenames[0])-1-indice
            if filenames[0][ct]=='/':
                break
        folder = filenames[0][:ct+1] +'AAA'
        Vmin_glob =-9999;Vmax_glob =9999
        df_news = []
        if conca == False:
            for i in range(len(files_mult[0][0])):
                list_interps = []
                for j in range(len(files_mult)):
                    df = files_mult[j][0][i]
                    colum = df.columns
                    x_data = array(df[colum[0]]); y_data = array(df[colum[1]])
                    if x_data[0]>0:
                        xnew = [];ynew = []
                        for i in range(len(x_data)):
                            xnew.append(x_data[len(x_data)-i-1])
                            ynew.append(y_data[len(y_data)-1-i])
                        x_data = array(xnew)
                        y_data = array(ynew)

                    f = interpolate.interp1d(x_data,y_data)
                    list_interps.append(f)
                    if j ==0:
                        vmin = x_data.min();vmax = x_data.max()
                        if x_data.min()>Vmin_glob:
                            Vmin_glob = x_data.min()
                        if x_data.max()<Vmax_glob:
                            Vmax_glob = x_data.max()
                    else:
                        if x_data.min()>vmin:
                            vmin = x_data.min()
                        if x_data.max()<vmax:
                            vmax = x_data.max()
                        if x_data.min()>Vmin_glob:
                            Vmin_glob = x_data.min()
                        if x_data.max()<Vmax_glob:
                            Vmax_glob = x_data.max()
                V_new = arange(vmin,vmax,0.005)
                
                for k in range(len(list_interps)):
                    if k ==0:
                        ymedia = array(list_interps[k](V_new))
                    else:
                        ymedia=(ymedia+array(list_interps[k](V_new)))/2

                V_new = V_new
                df_media = DataFrame(V_new,columns = ['V'])
                df_media['I'+str(i)]=ymedia
                df_news.append(df_media)
            files_data = [df_news,files_mult[0][1],[Vmin_glob,Vmax_glob]]
        elif conca == True:
            df_conca = []
            for j in range(len(files_mult)):
                if j ==0:
                    df = files_mult[j][0]
                    df_conca = df
                else:
                    df_conca=df_conca+df
            for i in range(len(files_mult[0][0])):
                for j in range(len(files_mult)):
                    try:
                        df = files_mult[j][0][i]
                        colum = df.columns
                        x_data = array(df[colum[0]])
                        if x_data[0]>0:
                            x_data = sort(x_data)
                        if j ==0:
                            vmin = x_data.min();vmax = x_data.max()
                            if x_data.min()>Vmin_glob:
                                Vmin_glob = x_data.min()
                            if x_data.max()<Vmax_glob:
                                Vmax_glob = x_data.max()
                        else:
                            if x_data.min()>vmin:
                                vmin = x_data.min()
                            if x_data.max()<vmax:
                                vmax = x_data.max()
                            if x_data.min()>Vmin_glob:
                                Vmin_glob = x_data.min()
                            if x_data.max()<Vmax_glob:
                                Vmax_glob = x_data.max()
                    except IndexError:
                        pass
            print(len(df_conca))
            files_data = [df_conca,list(map(lambda x:str(x),range(len(df_conca)))),[Vmin_glob,Vmax_glob]]
            
    else:
        files_data = load_file(folder)



global folder
global filenames
global files_data
folder = None  # Declare global variable first
filenames = None
global hist_path
hist_path = 'not_path'
global curve_glob
global smooth_glob
global delta_glob
global selec 
curve_glob = 0; smooth_glob = 0; delta_glob = 0
global save_var
save_var = True
selec = {}





def didv(x,y):
    h = x[1]-x[0]
    deri_y = []; deri_x =[]
    for i in range(1,len(x)-1):
        d = (y[i+1]-y[i-1])/(2*h)
        deri_x.append(x[i])
        deri_y.append(d)
    deri_y=array(deri_y)
    return [array(deri_x),deri_y/deri_y.max()]

def i_V(x,y):
  I =[]; V= []
  for i in range(1,len(x)-1):
    V.append(x[i])
    I.append(y[i])
  return [array(V),array(I)]

def gap_type(dx,dy,delta):
    f = interpolate.interp1d(dx, dy)
    marker1 = False; marker2 = False

    for i in range(len(dx)-1):
        if dx[0]<0:
            if dx[i]<=0 and dx[i+1]>=0:
               indice_x0 = i
               break
    marker1 = False; marker2 = False

    for i in range(len(dx)):
        if dx[0]<0:
          if i <= indice_x0:
            j= indice_x0-i
            if f(dx[j])<= delta and marker1 == False:
                xmin = dx[j]
            else:
               marker1 = True

          elif i > indice_x0:
            j= i 
            if f(dx[j])<= delta and marker2 == False:
                xmax = dx[j]
            else:
               marker2 = True
               
    try:
        gap = xmax-xmin
    except UnboundLocalError:
        xmin = 0
        xmax = 0
        gap = 0
    typ = abs(xmax) - abs(xmin)
    return [round(gap,2),round(typ,2),xmin,xmax]

def inter_x(x,y,z,dx = 100, dy= 100):

    interp = interpolate.RegularGridInterpolator((x,y),z)
    xnew = linspace(x.min(),x.max(),dx)
    ynew = linspace(y.min(),y.max(),dy)
    
    M_int = []
    for i in range(len(xnew)):
        pts = []
        for j in range(len(ynew)):
            pts.append([xnew[i],ynew[j]])
        pts = array(pts)
        col = interp(pts)
        M_int.append(array(col))
    
    return [xnew,ynew,array(M_int)]

def to_table(path_files):
    files = listdir(path_files)
    arq_I = open(path_files+'Dataframe_I_complete.csv','w')
    arq_didv = open(path_files+'Dataframe_dIdv_complete.csv','w')
    lines_I = []
    lines_didv = []
    marker=False
    marker2 = True
    for item in files:
        if '.txt' in item:
            df = read_csv(path_files+item)
            number = ''
            for car in item:
                if car=='_':
                    break
                number+=car
            col = df.columns
            x=df[col[0]];y=df[col[1]];dy=df[col[2]]
            dy=dy/dy.max()
            if marker == False:
                tam = len(x)
                xlimmin = x.min()
                xlimmax = x.max()
                lines_I.append([col[0]+'_'+number,',',col[1]+'_'+number])
                lines_didv.append([col[0]+'_'+number,',',col[2]+'_'+number])
                marker = True
                for j in range(len(x)):
                    lines_I.append([x[j],',',y[j]])
                    lines_didv.append([x[j],',',dy[j]])
            else:
                if x.min()>=xlimmin:
                    xlimmin=x.min()
                if x.max()<=xlimmax:
                    xlimmax=x.max()
                lines_I[0] = lines_I[0]+ [',',col[0]+'_'+number,',',col[1]+'_'+number]
                lines_didv[0] = lines_didv[0]+ [',',col[0]+'_'+number,',',col[2]+'_'+number]

                if len(x)<=tam:
                    for k in range(len(x)):
                        lines_I[k+1] = lines_I[k+1]+ [',',x[k],',',y[k]]
                        lines_didv[k+1] = lines_didv[k+1]+ [',',x[k],',',dy[k]]
                else:
                    for k in range(len(x)):
                        if k <tam:
                            lines_I[k+1] = lines_I[k+1]+ [',',x[k],',',y[k]]
                            lines_didv[k+1] = lines_didv[k+1]+ [',',x[k],',',dy[k]]
                        else:
                            lines_I.append([x[j],',',y[j]])
                            lines_didv.append([x[j],',',y[j]])
                    tam=len(x)
    for line in lines_I:
        line = list(map(lambda x:str(x),line))
        l = ''
        for c in line:
            l+=c 
        arq_I.writelines(l+'\n')
    arq_I.close()
    for line in lines_didv:
        line = list(map(lambda x:str(x),line))
        l = ''
        for c in line:
            l+=c 
        arq_didv.writelines(l+'\n')
    arq_didv.close()

    for item in files:
        if '.txt' in item:
            df = read_csv(path_files+item)
            number = ''
            for car in item:
                if car=='_':
                    break
                number+=car

            col = df.columns
            x=df[col[0]];y=df[col[1]];dy=df[col[2]]
            dy=dy/dy.max()
            if marker2:
                xnew  = arange(xlimmin,xlimmax,0.01)
                f = interpolate.interp1d(x,y)
                g = interpolate.interp1d(x,dy)
                df2 = DataFrame({'V':xnew,'I_'+number:f(xnew)})
                df3 = DataFrame({'V':xnew,'didv_'+number:g(xnew)})
                marker2=False
            else:
                f = interpolate.interp1d(x,y)
                g = interpolate.interp1d(x,dy)
                df2['I_'+number]=f(xnew)
                df3['didv_'+number]=g(xnew)
    df2 = df2.set_index('V')
    df3 = df3.set_index('V')
    df2.to_csv(path_files+'Dataframe_I_limeted_by_V.csv')
    df3.to_csv(path_files+'Dataframe_didv_limeted_by_V.csv')

     
def Display():
        #file = load_file(folder)
        file = files_data
        def plot_curve(file,curve = 0,smooth = 5,delta = 10,resolution=0.010):
                global save_var
                global curve_glob
                global smooth_glob
                global delta_glob
                global selec 
                curve_glob = curve; smooth_glob = smooth; delta_glob = delta
            
                


                curve = int(curve)
                fig,ax= plt.subplots(1,2,figsize=(20,8))
                dfs = file[0]
                columns = dfs[curve].columns
                x = dfs[curve][columns[0]];y = dfs[curve][columns[1]]*pow(10,9)
                p = int(smooth*len(y)/100)
                if p%2==0:
                    p+=1
                    y = savgol_filter(y,p,1)
                elif p==0:
                    pass
                else:
                    y = savgol_filter(y,p,1)

                ax[0].plot(x,y)
                ax[0].set_xlabel('Sample bias (V)')
                ax[0].set_ylabel('Current (nA)')

                dx,dy = didv(x,y)
                gap,typ,xmin,xmax = gap_type(dx,dy,delta/100)
                if abs(round(typ,3))<=resolution:
                    tipo = 'neutro'
                elif typ<-resolution:
                    tipo = 'n'
                else:
                    tipo = 'p'
                dyinterp = interpolate.interp1d(dx,dy)
                ymin = dyinterp(xmin)
                ymax = dyinterp(xmax)
                ax[1].scatter([xmin,xmax],[ymin,ymax],s = 50, color = 'red')
                ax[1].plot(dx,dy, label = 'Gap '+ str(gap)+ ': Type ' + tipo)
                ax[1].set_xlabel('Sample bias (V)')
                ax[1].set_ylabel('dI/dV (arb. units)')
                ax[1].legend()    
        
        curve_slider=widgets.widgets.IntSlider(
		value=0,min=0,max=len(files_data[0])-1,	step=1,description='Select Curve: ',continuous_update=False,layout=widgets.Layout(width='400px')	)  
        smoothingSlider=widgets.widgets.FloatSlider(
		value=5,min=.5,max=20,	step=.5,description='Smoothing: ',continuous_update=False,layout=widgets.Layout(width='400px')	)  
        deltaSlider=widgets.widgets.FloatSlider(
		value=5,min=.5,max=20,	step=.5,description='Threshold: ',continuous_update=False,layout=widgets.Layout(width='400px')	)  
        resolutionSlider = widgets.FloatText(
        value=0.010,
        description='Resolution of Doping Neutral (V):',
        disabled=False,layout=widgets.Layout(width='400px')	
)

        widgets.interact(plot_curve, file = widgets.fixed(file),  curve=curve_slider, smooth = smoothingSlider,delta = deltaSlider,resolution = resolutionSlider)
        print(curve_glob,smooth_glob,delta_glob)





def select_sts(path_file, n = [],smooth = 5,delta = 10,resolution = 0.01):
            global hist_path
            #file = load_file(path_file)
            file = files_data
            folder_save = 'sts_saves'
            for i in range(1,len(path_file[:-4])):
                if path_file[len(path_file[:-4]) -i] == '/':
                    ct = len(path_file[:-4]) -i
                    break
            try:
                #folder_name = path.join(folder_save,path_file[:-4][ct:])
                folder_name= folder_save+path_file[:-4][ct:]
            except UnboundLocalError:
                ct = 0
                #folder_name = path.join(folder_save,path_file[ct:-4])
                folder_name= folder_save+'/'+ path_file[:-4][ct:]
            try: 
                mkdir(folder_save )
            except FileExistsError:
                pass
                
            paste =folder_name
            try:
                mkdir(paste)
            except FileExistsError:
                for root, dirs, files_list in walk(paste):
                    for f in files_list:
                        #if file.endswith('.txt'):
                        remove(path.join(root, f))
                          
            hist ={'Curve':[],'Gap(V)':[] , 'Dop(Type)':[],'Dop(Value)':[]}
            for i in range(len(file[0])):
                if (i in n) == False:
                        name = path.join(paste,file[1][i])
                        x= file[0][i][file[0][i].columns[0]];y = file[0][i][file[0][i].columns[1]]*pow(10,9)
                        p = int(smooth*len(y)/100)
                        if p%2==0:
                            p+=1
                            y = savgol_filter(y,p,1)
                        elif p==0:
                            pass
                        else:
                            y = savgol_filter(y,p,1)
                        dx,dy = didv(x,y)
                        gap,typ,xmin,xmax = gap_type(dx,dy,delta/100)
                        hist['Curve'].append(i)
                        hist['Gap(V)'].append(round(gap,3))
                        hist['Dop(Value)'].append(round(typ,3))
                        if abs(round(typ,3))<=resolution:
                            tipo = 'neutro'
                        elif typ<-resolution:
                            tipo = 'n'
                        else:
                            tipo = 'p'
                        hist['Dop(Type)'].append(tipo)
                        f = interpolate.interp1d( file[0][i][file[0][i].columns[0]],file[0][i][file[0][i].columns[1]])
                        g = interpolate.interp1d(dx,dy)
                        xnew = arange(dx.min(),dx.max()-0.01,0.01)
                        df_new = DataFrame({'V':xnew,'I(nA)':f(xnew),'didv':g(xnew),'gap': str(gap),'tipo':str(tipo)}   )
                        df_new = df_new.set_index('V')
                        if ct ==0:
                            df_new.to_csv(name +'_'+path_file[:-4][ct:]+'.txt') 
                        else:
                            df_new.to_csv(name +'_'+path_file[:-4][ct+1:]+'.txt')

            df_hist = DataFrame(hist)
            df_hist = df_hist.set_index('Curve')
            df_hist.to_csv(paste+'/'+'histogram.csv')
            hist_path = paste+'/'+'histogram.csv'
            print("arquivos salvos na pasta "+ paste)
            to_table(paste+'/')
   
def Save_data():
    file = files_data
    for i in range(len(file[0])):
            selec[i] = True
    
    def str_to_int(A):
        A_new = []
        for item in A:
            try:
                A_new.append(int(item))
            except ValueError:
                pass
        return A_new

    def save_files(list_n,salvar = False,smooth = 5,delta = 5,resolution=0.01):

        list_n = list_n.split(',')
        n_new = str_to_int(list_n)
        if salvar:
            select_sts(folder,n = n_new,smooth = smooth,delta = delta,resolution=resolution)
            print('Files saved')

        
    
    list_n = widgets.Textarea(
    value='',    placeholder="Write down the number of the files that you DON'T want to save. Separated by comma.",    
    description="List of curve numbers: ",    disabled=False, layout=widgets.Layout(width='400px'))
    print("Write down the number of the files that you DON'T want to save. Separated by comma.")
    save_buttom= widgets.ToggleButton(
    value=False,
    continuous_update=tuple,
    description='Save file and make a report',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Description',
    icon='check',
    layout=widgets.Layout(width='400px')
)
    smoothingSlider=widgets.widgets.FloatSlider(
		value=5,min=.5,max=20,	step=.5,description='Smoothing (%): ',continuous_update=False,layout=widgets.Layout(width='400px')	)  
    deltaSlider=widgets.widgets.FloatSlider(
		value=5,min=.5,max=20,	step=.5,description='Threshold (%): ',continuous_update=False,layout=widgets.Layout(width='400px')	)  
    resolutionSlider = widgets.FloatText(
    value=0.010,
    description='Resolution of Doping Neutral (V):',
    disabled=False,layout=widgets.Layout(width='400px')	
)


    widgets.interact(save_files, list_n = list_n,salvar = save_buttom,smooth = smoothingSlider,delta = deltaSlider,resolution = resolutionSlider)
    
def hist_plot():
    font = {'size'   : 14}
    matplotlib.rc('font', **font)
    if hist_path == 'not_path':
        gui = Tk()
        gui.geometry("400x400")
        gui.title('Nanosurf STS Data Analise by Rafael Reis Barreto')
        def getFolderPath():
            global hist_path
            hist_path = filedialog.askopenfilename()
            print("File: ",hist_path)
            print("Uploaded")
            gui.destroy()

        btnFind = ttk.Button(gui, text="Open a histogram file", command=getFolderPath)
        btnFind.grid(row=1,column=1)
        gui.mainloop()
    hist_file = read_csv(hist_path)


    def plot_hist(hist_file_col,bins,label,monocolor,rwidth):
            fig, ax = plt.subplots(figsize = (10,8))
            if monocolor:
                N,n_bins,patches =ax.hist(hist_file_col,bins = bins,rwidth= rwidth)
                # We'll color code by height, but you could use any scalar
                hist_file_col=array(hist_file_col)
                fracs = array(sorted(hist_file_col))/hist_file_col.max()

                # we need to normalize the data to 0..1 for the full range of the colormap
                norm = matplotlib.colors.Normalize(fracs.min(), fracs.max())

                # Now, we'll loop through our objects and set the color of each accordingly
                for thisfrac, thispatch in zip(fracs, patches):
                    color = plt.cm.viridis(norm(thisfrac))
                    thispatch.set_facecolor(color)
            else:
                ax.hist(hist_file_col,bins = bins,edgecolor='black',rwidth= rwidth)


            ax.set_xlabel(label)
            ax.set_ylabel('Counting')
            de = rwidth*(hist_file_col.max()-hist_file_col.min())/bins     
            print('Voltage width of each bar: %s (V)'%(round(de,3)))



    box_layout = widgets.Layout(
			border='dashed 1px gray',
			margin='0px 10px 10px 0px',
			padding='5px 5px 5px 5px',
			width='600px')


    style = {'description_width': 'initial'}

    panel=[{},{}]
    fig= []
    axes=[]

    
    for axis in [0,1]:
        panel[axis]['bins']=widgets.IntSlider(value=10,min=1,max=100,	
                                            step=1,description='Bins: ',continuous_update=False,layout=widgets.Layout(width='400px')	)
        panel[axis]['histcolor']=widgets.Checkbox(value = False,description= 'Hist color by x axis',disable = False)
        panel[axis]['rwidth']=widgets.FloatSlider(value=0.9,min=0.1,max=1,	
                                            step=.1,description='rwidth: ',continuous_update=False,layout=widgets.Layout(width='400px')	)

    colums = [hist_file['Gap(V)'],hist_file['Dop(Value)']]
    label = ['Gap (V)','Doping, Shifting from 0 (V) ']
    for axis in [0,1]:
        panel[axis]['output']=widgets.interactive_output(plot_hist,{'hist_file_col':widgets.fixed(colums[axis]),
                                                                    'bins':panel[axis]['bins'],
                                                                    'label': widgets.fixed(label[axis]),
                                                                    'monocolor': panel[axis]['histcolor'],
                                                                    'rwidth': panel[axis]['rwidth']})
        panel[axis]['widget'] = widgets.VBox([panel[axis]['output'],panel[axis]['bins'], panel[axis]['histcolor'],panel[axis]['rwidth']],layout=box_layout)
        panel[axis]['widget'].children[0].layout.height = '600px'


    outputPanel = widgets.HBox([panel[0]['widget'],panel[1]['widget']],layout=widgets.Layout(width='1200px'))
    return outputPanel
    

def map_plot():
    font = {'size'   : 14}
    matplotlib.rc('font', **font)
    #file = load_file(folder)
    file = files_data
    def get_matrix(dfs,delta,nx=20,V=0):
        files = []
        for i in range(len(dfs)):
            columns = dfs[i].columns
            x = dfs[i][columns[0]];y = dfs[i][columns[1]]*pow(10,9)
            files.append([x,y])
        ny = int(len(dfs)/nx)
        M_didv = [];M_dop = [];M_gap = []
        for i in range(nx):
            col_didv = [];col_dop = [];col_gap = []
            for j in range(ny):
                x,y = files[j+i*ny]
                dx,dy = didv(x,y)
                gap,typ,xmin,xmax = gap_type(dx,dy,delta/100)
                dyinterp = interpolate.interp1d(dx,dy)

                col_didv.append(dyinterp(V))
                col_dop.append(round(typ,3))
                col_gap.append(round(gap,3))
            M_didv.append(array(col_didv));M_dop.append(array(col_dop));M_gap.append(array(col_gap))

        M_didv = array(M_didv);M_dop = array(M_dop);M_gap = array(M_gap)
        x = arange(nx);y=arange(ny)
        return [x,y,[M_didv,M_gap,M_dop]]

    def plot_mapa2(file,whichmap,delta = 5,interpolation= False,mult=2,cmap = 'viridis',nx = 20):
        x,y,mapas = get_matrix(file,delta,nx=nx)
        M=mapas[whichmap]

        fig,ax= plt.subplots(figsize=(10,8))

        if interpolation == True:
            nx = len(x);ny=len(y)

            x,y,M = inter_x(x,y,M,dx=mult*nx,dy = mult*ny)

        Y,X = meshgrid(y,x)
        im = ax.pcolormesh(X,Y,M,cmap = cmap)

        if whichmap==1:
            cbar = fig.colorbar(im)
            cbar.set_ticks([M.min(),M.max()],labels= ['Gap ','No Gap'])
        elif whichmap==2:
            cbar = fig.colorbar(im)
            cbar.set_ticks([M.min(),0,M.max()],labels= ['N ','Neutro','P'])

        #im2 = ax[2].pcolormesh(X,Y,M_dop,cmap = cmap)
        #cbar = fig.colorbar(im2)
        #cbar.set_ticks([M_dop.min(),0,M_dop.max()],labels= ['N ','Neutro','P'])

    def plot_mapa(file,whichmap,V = 0,delta = 5,interpolation= False,mult=2,cmap = 'viridis',nx =20):
        x,y,mapas = get_matrix(file,delta,V=V,nx = nx)
        M=mapas[whichmap]

        fig,ax= plt.subplots(figsize=(10,8))

        if interpolation == True:
            nx = len(x);ny=len(y)

            x,y,M = inter_x(x,y,M,dx=mult*nx,dy = mult*ny)

        Y,X = meshgrid(y,x)
        im = ax.pcolormesh(X,Y,M,cmap = cmap)
        cbar = fig.colorbar(im)


    box_layout = widgets.Layout(
			border='dashed 1px gray',
			margin='0px 10px 10px 0px',
			padding='5px 5px 5px 5px',
			width='600px')

    panel=[{},{},{}]
    fig= []
    axes=[]
    for axis in [0,1,2]:
        if axis ==0:
            panel[axis]['vslider']=widgets.widgets.FloatSlider(
		    value=0,min=file[2][0],max=file[2][1],	step=.2,description='Sample Bias (V): ',continuous_update=False,layout=widgets.Layout(width='300px')	)
        panel[axis]['deltaslider']=widgets.widgets.FloatSlider(
		value=5,min=.5,max=20,	step=.5,description='Threshold: ',continuous_update=False,layout=widgets.Layout(width='300px')	)  
        panel[axis]['interpolation']=widgets.Checkbox(value = False,description= 'Interpolation',disable = False)
        panel[axis]['mult']=widgets.widgets.IntSlider(
		value=2,min=1,max=20,	step=1,description='Multiplicity of interpolation ',continuous_update=False,layout=widgets.Layout(width='300px'))	
        panel[axis]['nx']=widgets.IntText(  value=20, description='Number of points per line. Nanosurf software',  disabled=False
)
        panel[axis]['colormap'] = widgets.Dropdown(
		options=['bone_r', 'inferno', 'viridis','plasma', 'cividis','gray','OrRd','PuBuGn','coolwarm','bwr','terrain'],
		value='viridis',
		description='Colormap:',
		)

    for axis in [0,1,2]:

        if axis ==0:
            panel[axis]['output']=widgets.interactive_output(plot_mapa,{'file':widgets.fixed(file[0]),
                                                                    'whichmap':widgets.fixed(axis),
                                                                    'V':panel[axis]['vslider'],
                                                                    'delta': panel[axis]['deltaslider'],
                                                                    'interpolation': panel[axis]['interpolation'],
                                                                    'mult': panel[axis]['mult'],
                                                                    'cmap':panel[axis]['colormap'],
                                                                    'nx':panel[axis]['nx']
                                                                    })
            panel[axis]['widget'] = widgets.VBox([panel[axis]['output'],panel[axis]['vslider'], panel[axis]['deltaslider'],
                                              panel[axis]['interpolation'],panel[axis]['mult'],panel[axis]['colormap'],panel[axis]['nx'] ],layout=box_layout)
            panel[axis]['widget'].children[0].layout.height = '400px'
        else:
            panel[axis]['output']=widgets.interactive_output(plot_mapa2,{'file':widgets.fixed(file[0]),
                                                                    'whichmap':widgets.fixed(axis),
                                                                    'delta': panel[axis]['deltaslider'],
                                                                    'interpolation': panel[axis]['interpolation'],
                                                                    'mult': panel[axis]['mult'],
                                                                    'cmap':panel[axis]['colormap'],
                                                                    'nx':panel[axis]['nx']
                                                                    })
            panel[axis]['widget'] = widgets.VBox([panel[axis]['output'],panel[axis]['deltaslider'],
                                              panel[axis]['interpolation'],panel[axis]['mult'],panel[axis]['colormap'],panel[axis]['nx'] ],layout=box_layout)
        panel[axis]['widget'].children[0].layout.height = '600px'


    outputPanel = widgets.HBox([panel[0]['widget'],panel[1]['widget'],panel[2]['widget']],layout=widgets.Layout(width='1800px'))
    return outputPanel

