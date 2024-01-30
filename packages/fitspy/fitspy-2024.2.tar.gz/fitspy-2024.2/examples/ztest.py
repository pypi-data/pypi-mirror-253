"""
module description
"""
from pathlib import Path
import tkinter as tk
import glob
import time
from multiprocessing import freeze_support

from fitspy.app.gui import fitspy_launcher, Appli


def lorentzian_user2(x, ampli, x0, fwhm):
    return ampli * fwhm ** 2 / (4 * ((x - x0) ** 2 + fwhm ** 2 / 4))


def linear_user2(x, slope, constant):
    return slope * x + constant


def ex0():
    dirname = Path(__file__).parent / "data" / "spectra_2"
    fname0 = dirname / "InP-1_42-P21_a.txt"
    fname1 = dirname / "InP-1_42-P21_b.txt"
    fname2 = dirname / "InP-1_42-P21_c.txt"
    fnames = [fname0, fname1, fname2]
    fname_json = dirname / "model_test_perfo.json"

    root = tk.Tk()
    appli = Appli(root)

    appli.add_items(fnames=fnames)
    model = appli.load_model(fname_json=fname_json)
    appli.apply_model(model)
    appli.save_results(dirname_res='results')

    fnames = glob.glob('results/*.txt')
    for fname in fnames:
        with open(fname, 'r') as fid:
            fid.readline()
            fid.readline()
            line = fid.readline()
            print(line[:-1])


def ex1():
    root = tk.Tk()
    appli = Appli(root)

    from lmfit.models import ExpressionModel
    from fitspy import MODELS, BKG_MODELS

    # mimic user-defined model from '%HOMEUSER%/Fitspy/model.txt'
    name = 'Lorentzian_user'
    expr = "ampli * fwhm ** 2 / (4 * ((x - x0) ** 2 + fwhm ** 2 / 4))"
    model = ExpressionModel(expr, independent_vars=['x'])
    model.__name__ = name
    MODELS.update({name: model})
    print(MODELS['Lorentzian_user'])

    # from fitspy.utils import load_models_from_txt
    # load_models_from_txt("models.txt", MODELS)
    # print(MODELS['Lorentzian_user'])

    # mimic user-defined bkg_model from '%HOMEUSER%/Fitspy/bkg_model.txt'
    name = 'Linear_user'
    expr = "slope * x + constant"
    bkg_model = ExpressionModel(expr, independent_vars=['x'])
    bkg_model.__name__ = name
    BKG_MODELS.update({name: bkg_model})

    # MODELS.update({'Lorentzian_user': lorentzian_user2})
    #
    # BKG_MODELS.update({'Linear_user': linear_user2})

    dirname = Path(__file__).parent / "data" / '2D_maps'
    str_map = dirname / 'ordered_map.txt'
    unstr_map = dirname / 'unordered_map.txt'

    appli.add_items(fnames=[str_map])

    fname_json = dirname / "model.json"

    appli.load_model(fname_json=fname_json)

    # root.mainloop()

    ncpus = 1
    appli.ncpus = ncpus

    t0 = time.time()
    # freeze_support()
    fnames = appli.spectra.fnames[:5 * ncpus]
    appli.apply_model(fnames=fnames)
    print(f'TCPU :{time.time() - t0}')

    root.mainloop()

    # appli.save_results(dirname_res='results2')
    #
    # fnames = glob.glob('results2/*.txt')
    # for fname in fnames:
    #     with open(fname, 'r') as fid:
    #         fid.readline()
    #         fid.readline()
    #         line = fid.readline()
    #         print(line[:-2])
    #
    # fnames = glob.glob('results2/*.csv')
    # for fname in fnames:
    #     with open(fname, 'r') as fid:
    #         fid.readline()
    #         line = fid.readline()
    #         print(line[:-2])
    #
    # root.mainloop()


if __name__ == '__main__':
    ex1()
