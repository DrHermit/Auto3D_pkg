from Auto3D.auto3D import options, main

if __name__ == "__main__":
    input_path = "example/files/smiles.smi"
    args = options(input_path, k=1)   #args specify the parameters for Auto3D 
    out = main(args)                  #main accepts the parameters and runs Auto3D