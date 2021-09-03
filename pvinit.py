import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--root','-r', dest='root', default='/data',type=str,help='absolute path of pv, default is /data')
parser.add_argument('--chain','-c', dest='chain',type=str,help='name of the chain\n  e.g. test-chain')
parser.add_argument('--nodes','-n', dest='nodes',nargs='+',type=str,help='name of the nodes\n  e.g. node1 node2 node3')
parser.add_argument('--clean','-cl', dest='clean',help='delete all files in node dir',action='store_true')
args = parser.parse_args()

allPath=os.path.join(args.root,'cita-cloud')
chainPath=os.path.join(allPath,args.chain)

if not os.path.exists(args.root):
    print('root path:',args.root,'does not exist')
    exit(1)

for node in args.nodes:
    nodePath=os.path.join(chainPath,node)
    print(nodePath)
    if not os.path.exists(nodePath): 
        # Path not exists
        os.makedirs(nodePath)
    else:
        if os.path.isdir(nodePath):
            if args.clean:
                # Delete all file in that path
                for fileOrDir in os.listdir(nodePath):
                    full=os.path.join(nodePath,fileOrDir)
                    if os.path.isdir(full):
                        shutil.rmtree(full)
                    else:
                        os.remove(full)
        else:
            # Path exists, but it is a file
            os.remove(nodePath)
            os.path.mkdir(nodePath)
                
        
        
    


