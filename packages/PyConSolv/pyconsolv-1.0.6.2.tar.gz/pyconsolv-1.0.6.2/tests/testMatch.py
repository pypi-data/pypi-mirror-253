from PyConSolv.misc.coordinateCheck import XYZMapper

if __name__ == '__main__':

    parser = XYZMapper('/home/rat/PYCONSOLV_DATA/ts/input.xyz.original')
    parser.mapXYZ('/home/rat/PYCONSOLV_DATA/ts/input.xyz')
    print(parser.mapAtom(2))
    print('done')