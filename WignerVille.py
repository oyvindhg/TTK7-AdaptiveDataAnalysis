from pytftb.tftb.processing.cohen import WignerVilleDistribution

# Wigner-Ville distribution
def WignerVille(S):

    wvd = WignerVilleDistribution(S)
    wvd.run()
    wvd.plot(show_tf=True, cmap='Blues')