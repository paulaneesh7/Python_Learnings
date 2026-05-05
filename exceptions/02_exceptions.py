
def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("Sorry, we don't have that flavour.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{flavour} chai is ready! Enjoy your drink.")
    finally:
        print("Thank you for visiting our chai shop!")


serve_chai("masala")  # Should prepare and serve masala chai
serve_chai("unknown")  # Should raise an error and handle it gracefully
