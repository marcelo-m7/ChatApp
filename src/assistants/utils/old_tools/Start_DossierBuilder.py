from ..Tools.DossierBuilder import start_dossier_builder
from Tools.VectorStoreBuilder import get_vector_store


def main():
    vector_store = get_vector_store()
    start_dossier_builder(vector_store=vector_store)

if __name__ == "__main__":
    main()
