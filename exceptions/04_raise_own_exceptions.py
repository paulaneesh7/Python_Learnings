

def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "cardamom"]:
        raise ValueError(f"Sorry, we don't have {flavour} chai.")
    print(f"Brewing {flavour} chai... Done!")



brew_chai("masala")  # Should brew masala chai
brew_chai("unknown")  # Should raise a ValueError and print the error message