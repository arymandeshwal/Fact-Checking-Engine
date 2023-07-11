import os
from rdflib import Graph
import sys

def conv2list_train():
    """
    Loads the training data and returns nested list of training data.
    """
    target_file = "fokg-sw-train-2023.nt"
    
    train = Graph()
    train.parse(target_file, format="nt")
    query = """
    SELECT ?st ?tv ?s ?p ?o
    WHERE{
        ?st a rdf:Statement .
        ?st ns1:hasTruthValue ?tv .
        ?st rdf:subject ?s .
        ?st rdf:predicate ?p .
        ?st rdf:object ?o .
    }
    """
    # Storing the triples in a list
    train_fc = []
    result = train.query(query)
    for row in result:
        train_fc.append([ row['st'], float(row['tv']), str(row['s']), str(row['p']), str(row['o'])])
    return train_fc

def conv2list_test():
    target_file = "fokg-sw-test-2023.nt"
    
    test = Graph()
    test.parse(target_file, format="nt")
    
    query = """
    SELECT ?st ?s ?p ?o
    WHERE{
        ?st a rdf:Statement .
        ?st rdf:subject ?s .
        ?st rdf:predicate ?p .
        ?st rdf:object ?o .
    }
    """
    
    # Storing the triples in a list
    test_fc = []
    result = test.query(query)
    for row in result:
        test_fc.append([ row['st'], str(row['s']), str(row['p']), str(row['o'])])
    
    return test_fc