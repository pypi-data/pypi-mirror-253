import multiprocessing as mp   # multi process
import multiprocessing.dummy as mpd #multi-threading
import subprocess

class Threading:
    def __init__(self, args=None):
        self.args=args

    #multiple threads by threads pool
    def pp_map_threads(self, func, args_list):
        t = self.args.threads_num
        print("Multiple threads = ", t)
        #t=1
        if t < 2:
            for par in args_list:
                func(par)
        else:
            #threads number
            pool = mpd.Pool(t)
            #pass one argument at a time 
            pool.map(func, args_list) 
            pool.close()
            pool.join()  
            
    #multiple process by process pool
    #Note: pass a function - and not a method - to the worker processes
    def pp_map_process(self, func, args_list):
        t = self.args.threads_num
        print("Multiple processes: ", t)
        #t=1
        if t < 2:
            for par in args_list:
                func(par)
        else:
            #process number
            pool = mp.Pool(processes=t)
            #pass one argument at a time 
            pool.map(func, args_list)
            pool.close()
            pool.join()  


    @staticmethod
    def run_tool(command):
        print("@@@@@@@@@@@@", command)
        output="NA"
        output=subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True).stdout.read()  
        print(output)
        return output
