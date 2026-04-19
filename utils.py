import matplotlib.pyplot as plt


def get_saison(mois):
    """Associe un mois à une saison."""
    if mois in [12, 1, 2]:
        return "Hiver"
    elif mois in [3, 4, 5]:
        return "Printemps"
    elif mois in [6, 7, 8]:
        return "Été"
    else:

        return "Automne"


def plot_regularite_moyenne(df, variable, xlabel, title, xticks=None):
    """Calcule et trace la régularité moyenne selon une variable donnée."""
    regularite = (
        df.groupby(variable, as_index=False)["regularite_arrivee"]
        .mean()
    )

    plt.figure(figsize=(8, 5))
    plt.plot(
        regularite[variable],
        regularite["regularite_arrivee"],
        marker="o"
    )
    plt.xlabel(xlabel)
    plt.ylabel("Régularité moyenne")
    plt.title(title)

    if xticks is not None:
        plt.xticks(xticks)

    plt.show()

    return regularite