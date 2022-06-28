import argparse

def add_common_bsm_arguments(parser, DEFAULTS):
    
    ##### file containing the parameters
    parser.add_argument("--param-file", type=str, help="file containing parameters definitions")

    ##### dark sector spectrum
    parser.add_argument("--mzprime", type=float, help="Z' mass")
    parser.add_argument("--mhprime", type=float, help="h' mass")
    parser.add_argument("--m4", type=float, help="mass of the fourth neutrino")
    parser.add_argument("--m5", type=float, help="mass of the fifth neutrino")
    parser.add_argument("--m6", type=float, help="mass of the sixth neutrino")

    parser.add_argument("--HNLtype", type=str.lower, help="HNLtype: dirac or majorana", choices=DEFAULTS._choices['HNLtype'])

    ##### TMM in GeV^-1
    parser.add_argument("--mu_tr_e4", type=float, help="TMM mu_tr_e4")
    parser.add_argument("--mu_tr_e5", type=float, help="TMM mu_tr_e5")
    parser.add_argument("--mu_tr_e6", type=float, help="TMM mu_tr_e6")

    parser.add_argument("--mu_tr_mu4", type=float, help="TMM mu_tr_mu4")
    parser.add_argument("--mu_tr_mu5", type=float, help="TMM mu_tr_mu5")
    parser.add_argument("--mu_tr_mu6", type=float, help="TMM mu_tr_mu6")

    parser.add_argument("--mu_tr_tau4", type=float, help="TMM mu_tr_tau4")
    parser.add_argument("--mu_tr_tau5", type=float, help="TMM mu_tr_tau5")
    parser.add_argument("--mu_tr_tau6", type=float, help="TMM mu_tr_tau6")

    parser.add_argument("--mu_tr_44", type=float, help="TMM mu_tr_44")
    parser.add_argument("--mu_tr_45", type=float, help="TMM mu_tr_45")
    parser.add_argument("--mu_tr_46", type=float, help="TMM mu_tr_46")

    parser.add_argument("--mu_tr_55", type=float, help="TMM mu_tr_55")
    parser.add_argument("--mu_tr_56", type=float, help="TMM mu_tr_56")

    parser.add_argument("--mu_tr_66", type=float, help="TMM mu_tr_66")

    ##### Scalar vertices
    parser.add_argument("--s_e4", type=float, help="scalar vertex s_e4")
    parser.add_argument("--s_e5", type=float, help="scalar vertex s_e5")
    parser.add_argument("--s_e6", type=float, help="scalar vertex s_e6")

    parser.add_argument("--s_mu4", type=float, help="scalar vertex s_mu4")
    parser.add_argument("--s_mu5", type=float, help="scalar vertex s_mu5")
    parser.add_argument("--s_mu6", type=float, help="scalar vertex s_mu6")

    parser.add_argument("--s_tau4", type=float, help="scalar vertex s_tau4")
    parser.add_argument("--s_tau5", type=float, help="scalar vertex s_tau5")
    parser.add_argument("--s_tau6", type=float, help="scalar vertex s_tau6")

    parser.add_argument("--s_44", type=float, help="scalar vertex s_44")
    parser.add_argument("--s_45", type=float, help="scalar vertex s_45")
    parser.add_argument("--s_46", type=float, help="scalar vertex s_46")

    parser.add_argument("--s_55", type=float, help="scalar vertex s_55")
    parser.add_argument("--s_56", type=float, help="scalar vertex s_56")

    parser.add_argument("--s_66", type=float, help="scalar vertex s_66")


def add_three_portal_arguments(parser, DEFAULTS):
    ##### neutral lepton mixing
    parser.add_argument("--Ue4", type=float, help="Ue4")
    parser.add_argument("--Ue5", type=float, help="Ue5")
    parser.add_argument("--Ue6", type=float, help="Ue6")

    parser.add_argument("--Umu4", type=float, help="Umu4")
    parser.add_argument("--Umu5", type=float, help="Umu5")
    parser.add_argument("--Umu6", type=float, help="Umu6")

    parser.add_argument("--Utau4", type=float, help="Utau4")
    parser.add_argument("--Utau5", type=float, help="Utau5")
    parser.add_argument("--Utau6", type=float, help="Utau6")

    parser.add_argument("--UD4", type=float, help="UD4")
    parser.add_argument("--UD5", type=float, help="UD5")
    parser.add_argument("--UD6", type=float, help="UD6")

    ##### dark coupling choices
    parser.add_argument("--gD", type=float, help="U(1)_d dark coupling")
    parser.add_argument("--alphaD", type=float, help="U(1)_d  alpha_dark = (g_dark^2 /4 pi)")

    ##### kinetic mixing options
    parser.add_argument("--epsilon", type=float, help="epsilon")
    parser.add_argument("--epsilon2", type=float, help="epsilon^2")
    parser.add_argument("--alpha_epsilon2", type=float, help="alpha_QED*epsilon^2")
    parser.add_argument("--chi", type=float, help="chi")

    parser.add_argument("--theta", type=float, help="Scalar mixing angle between h-h'")



def add_generic_bsm_arguments(parser, DEFAULTS):

    ##### Z boson couplings
    parser.add_argument("--c_e4", type=float, help="SM Z boson vertex c_e4 ")
    parser.add_argument("--c_e5", type=float, help="SM Z boson vertex c_e5 ")
    parser.add_argument("--c_e6", type=float, help="SM Z boson vertex c_e6 ")
    parser.add_argument("--c_mu4", type=float, help="SM Z boson vertex c_mu4 ")
    parser.add_argument("--c_mu5", type=float, help="SM Z boson vertex c_mu5 ")
    parser.add_argument("--c_mu6", type=float, help="SM Z boson vertex c_mu6 ")
    parser.add_argument("--c_tau4", type=float, help="SM Z boson vertex c_tau4 ")
    parser.add_argument("--c_tau5", type=float, help="SM Z boson vertex c_tau5 ")
    parser.add_argument("--c_tau6", type=float, help="SM Z boson vertex c_tau6 ")
    parser.add_argument("--c_44", type=float, help="SM Z boson vertex c_44 ")
    parser.add_argument("--c_45", type=float, help="SM Z boson vertex c_45 ")
    parser.add_argument("--c_46", type=float, help="SM Z boson vertex c_46 ")
    parser.add_argument("--c_55", type=float, help="SM Z boson vertex c_55 ")
    parser.add_argument("--c_56", type=float, help="SM Z boson vertex c_56 ")
    parser.add_argument("--c_66", type=float, help="SM Z boson vertex c_66 ")

    ##### Z' vector couplings
    parser.add_argument("--d_e4", type=float, help="Z' vector vertex d_e4 ")
    parser.add_argument("--d_e5", type=float, help="Z' vector vertex d_e5 ")
    parser.add_argument("--d_e6", type=float, help="Z' vector vertex d_e6 ")
    parser.add_argument("--d_mu4", type=float, help="Z' vector vertex d_mu4 ")
    parser.add_argument("--d_mu5", type=float, help="Z' vector vertex d_mu5 ")
    parser.add_argument("--d_mu6", type=float, help="Z' vector vertex d_mu6 ")
    parser.add_argument("--d_tau4", type=float, help="Z' vector vertex d_tau4 ")
    parser.add_argument("--d_tau5", type=float, help="Z' vector vertex d_tau5 ")
    parser.add_argument("--d_tau6", type=float, help="Z' vector vertex d_tau6 ")
    parser.add_argument("--d_44", type=float, help="Z' vector vertex d_44 ")
    parser.add_argument("--d_45", type=float, help="Z' vector vertex d_45 ")
    parser.add_argument("--d_46", type=float, help="Z' vector vertex d_46 ")
    parser.add_argument("--d_55", type=float, help="Z' vector vertex d_55 ")
    parser.add_argument("--d_56", type=float, help="Z' vector vertex d_56 ")
    parser.add_argument("--d_66", type=float, help="Z' vector vertex d_66 ")

    ##### Charge particle couplings
    parser.add_argument("--ceV", type=float, help="SM Z boson vector vertex to charged leptons ceV")
    parser.add_argument("--ceA", type=float, help="SM Z boson axial vertex to charged leptons ceA")
    parser.add_argument("--cuV", type=float, help="SM Z boson vector vertex to up quark cuV")
    parser.add_argument("--cuA", type=float, help="SM Z boson axial vertex to up quark cuA")
    parser.add_argument("--cdV", type=float, help="SM Z boson vector vertex to down quark cdV")
    parser.add_argument("--cdA", type=float, help="SM Z boson axial vertex to down quark cdA")

    parser.add_argument("--deV", type=float, help="Z' vector vertex to charged leptons deV")
    parser.add_argument("--deA", type=float, help="Z' axial vertex to charged leptons deA")
    parser.add_argument("--duV", type=float, help="Z' vector vertex to up quark duV")
    parser.add_argument("--duA", type=float, help="Z' axial vertex to up quark duA")
    parser.add_argument("--ddV", type=float, help="Z' vector vertex to down quark ddV")
    parser.add_argument("--ddA", type=float, help="Z' axial vertex to down quark ddA")
    
    parser.add_argument("--deS", type=float, help="h' scalar vertex to charged leptons deS")
    parser.add_argument("--deP", type=float, help="h' pseudoscalar vertex to charged leptons deP")
    parser.add_argument("--duS", type=float, help="h' scalar vertex to up quark duS")
    parser.add_argument("--duP", type=float, help="h' pseudoscalar vertex to up quark duP")
    parser.add_argument("--ddS", type=float, help="h' scalar vertex to down quark ddS")
    parser.add_argument("--ddP", type=float, help="h' pseudoscalar vertex to down quark ddP")

    parser.add_argument("--cprotonV", type=float, help="SM Z boson vector vertex to charged leptons ceV")
    parser.add_argument("--cneutronA", type=float, help="SM Z boson axial vertex to charged leptons ceA")

    parser.add_argument("--dprotonV", type=float, help="Z' vector vertex to charged leptons deV")
    parser.add_argument("--dneutronA", type=float, help="Z' axial vertex to charged leptons deA")

    parser.add_argument("--dprotonS", type=float, help="h' scalar vertex to charged leptons dSe")
    parser.add_argument("--dneutronP", type=float, help="h' pseudoscalar vertex to charged leptons dPe")

def add_scope_arguments(parser, DEFAULTS):
    
    ##### visible final states in HNL decay
    parser.add_argument("--decay_product", type=str.lower, help="decay process of interest", choices=DEFAULTS._choices['decay_product'])

    ##### experiments    
    parser.add_argument("--exp", type=str.lower, help="experiment file path or keyword")
                                                                    
    ##### scattering types
    parser.add_argument("--nopelastic", help="do not generate proton elastic events", action="store_true")
    parser.add_argument("--nocoh", help="do not generate coherent events", action="store_true")
    parser.add_argument("--include_nelastic", help="generate neutron elastic events", action="store_true")

    parser.add_argument("--noHC", help="do not include helicity conserving events", action="store_true")
    parser.add_argument("--noHF", help="do not include helicity flipping events", action="store_true")

    parser.add_argument('--nu_flavors', type=str.lower, action='store', nargs='+', choices=DEFAULTS._choices['nu_flavors'])



def add_mc_arguments(parser, DEFAULTS):

    ##### run related arguments
    parser.add_argument("--loglevel", type=str.lower, help="Logging level")
    parser.add_argument("--verbose", help="Verbose for logging", action="store_true")
    parser.add_argument("--logfile", type=str, help="Path to logfile. If not set, use std output.")

    ##### Vegas parameters 
    parser.add_argument("--neval", type=int, help="number of evaluations of integrand")
    parser.add_argument("--nint", type=int, help="number of adaptive iterations")
    parser.add_argument("--neval_warmup", type=int, help="number of evaluations of integrand in warmup")
    parser.add_argument("--nint_warmup", type=int, help="number of adaptive iterations in warmup")

    ##### program options
    parser.add_argument("--pandas", help="If true, prints pandas dataframe to .pckl files", action="store_true")
    parser.add_argument("--parquet", help="If true, prints pandas dataframe to .parquet files. Loses metadata in attrs.", action="store_true")
    parser.add_argument("--numpy", help="If true, prints events as ndarrays in a .npy file", action="store_true")
    parser.add_argument("--hepevt", help="If true, unweigh events and print them in HEPEVT-formatted text files", action="store_true")
    parser.add_argument("--hepmc3", help="If true, prints events to HepMC3 format.", action="store_true")
    parser.add_argument("--hepevt_unweigh", help="unweigh events when printing in HEPEVT format (needs large statistics)", action="store_true")
    parser.add_argument("--unweighed_hepevt_events", type=int, help="number of unweighed events to accept in HEPEVT format. Has to be much smaller than neval for unweigh procedure to work.")

    parser.add_argument("--sparse", help="drop all information in the event except for visible particle momenta, neutrino energy, and weights.", action="store_true")
    parser.add_argument("--print_to_float32", help="Use float32 instead of default float64 when printing output to save storage space.", action="store_true")

    parser.add_argument("--enforce_prompt", help="forces the particles to decay promptly", action="store_true")
    parser.add_argument("--make_summary_plots", help="generate summary plots of kinematics", action="store_true")
    parser.add_argument("--path", type=str, help="path where to save run's outputs")
    parser.add_argument("--seed", type=int, help="numpy seed to be used by vegas.")