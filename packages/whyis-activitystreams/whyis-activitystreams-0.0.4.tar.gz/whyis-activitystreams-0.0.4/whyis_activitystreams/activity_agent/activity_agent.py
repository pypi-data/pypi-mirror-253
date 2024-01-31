from whyis.autonomic import UpdateChangeService
from whyis.namespace import NS

from whyis.plugin import Plugin
import rdflib
from flask import current_app


prefixes = dict(
    skos = rdflib.URIRef("http://www.w3.org/2004/02/skos/core#"),
    foaf = rdflib.URIRef("http://xmlns.com/foaf/0.1/"),
    text = rdflib.URIRef("http://jena.apache.org/fulltext#"),
    schema = rdflib.URIRef("http://schema.org/"),
    owl = rdflib.OWL,
    rdfs = rdflib.RDFS,
    rdf = rdflib.RDF,
    dc = rdflib.URIRef("http://purl.org/dc/terms/"),
    ao = rdflib.URIRef("http://purl.org/arclight/ontology/"),
    ov = rdflib.URIRef("http://open.vocab.org/terms/"),
    act = rdflib.URIRef("https://www.w3.org/ns/activitystreams#"),
    mediatype = rdflib.URIRef("https://www.iana.org/assignments/media-types/"),
    pv = rdflib.URIRef("http://purl.org/net/provenance/ns#"),
    sio = rdflib.URIRef("htttp://semanticscience.org/resource/")
)

class ActivityAgent(UpdateChangeService):
    activity_class = NS.whyis.ActivityResolving # resolving activities
    
    def get_query(self):
        return '''select distinct ?resource where {
            ?resource rdf:type [ rdfs:subClassOf* act:Object ] .
        }'''
        
    def get_context(self, i):
        context = []
        for s, p, o in i.graph.triples((i.identifier,None,None)):
            if p not in self.predicates:
                if isinstance(p, rdflib.Literal):
                    if o.datatype in self.context_datatypes:
                        context.append(o.value)
        return '\n'.join(context)
    
    def process(self, i, o):
        context = self.get_context(i)
        o.add(rdf.type,act.Object)
