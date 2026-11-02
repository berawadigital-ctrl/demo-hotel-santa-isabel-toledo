# Contenido de la demo Hotel Santa Isabel (Toledo) (es/en/fr/de). Hechos de hotelsantaisabeltoledo.es leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Dobles con vistas y Romántica','Superiores, Clásicas e Individual'],'en':['Doubles with views and Romantic','Superior, Classic and Single'],'fr':['Doubles avec vue et Romantique','Supérieures, Classiques et Individuelle'],'de':['Doppelzimmer mit Aussicht und Romantik','Superior, Klassik und Einzelzimmer']}
RD={
'es':['La Doble Romántica mira a la Catedral; la Doble Estándar con vistas tiene un balcón sobre la ciudad. Algunas conservan techos de madera con escudos del siglo XV.','Superiores amplias de 22 m² con zona de estar y balcones, ideales para familias; Clásicas al patio de flores e Individual Clásica para viajar solo.'],
'en':['The Romantic Double looks onto the Cathedral; the Standard Double with views has a balcony over the city. Some keep wooden ceilings with 15th-century coats of arms.','Spacious 22 m² Superiors with a seating area and balconies, ideal for families; Classic rooms onto the flower patio and a Classic Single for solo travellers.'],
'fr':['La Double Romantique donne sur la cathédrale ; la Double Standard avec vue a un balcon sur la ville. Certaines gardent des plafonds en bois aux blasons du XVe siècle.','Supérieures spacieuses de 22 m² avec coin salon et balcons, idéales en famille ; Classiques sur le patio fleuri et Individuelle Classique pour voyager seul.'],
'de':['Das romantische Doppelzimmer blickt auf die Kathedrale; das Standard-Doppelzimmer mit Aussicht hat einen Balkon über der Stadt. Manche bewahren Holzdecken mit Wappen aus dem 15. Jh.','Geräumige Superior-Zimmer mit 22 m², Sitzecke und Balkonen, ideal für Familien; Klassik-Zimmer zum Blumenpatio und ein klassisches Einzelzimmer für Alleinreisende.']}
ART={
'hero':('arches',9981,['#2b1d14','#d9a35a','#f1d29a','#8a5a2e','#6e4622','#3a2410']),
'intro':('columns',9982,['#f2ece2','#faf6ee','#8a5a2e','#6e4622','#3a2410']),
'r1':('arches',9991,['#f0e9de','#c99350','#8a5a2e','#6e4622','#3a2410']),
'r2':('skyline',9992,['#2b1d14','#e0aa64','#f4d7a6','#9a6a3e','#7a5230','#40281a']),
'g1':('skyline',9993,['#2b1d14','#d9a35a','#f1d29a','#8a5a2e','#6e4622','#3a2410']),
'g2':('arches',9994,['#f0ece4','#f9f5ee','#9c6a36','#6a4a2a','#3a2a18']),
'g3':('hills',9995,['#ece7da','#f1e2c3','#d6a160','#a8a07e','#7c7458','#55503c']),
'g4':('columns',9996,['#2b1d14','#e0aa64','#f4d7a6','#9a6a3e','#7a5230','#40281a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Santa Isabel · Hotel familiar en el casco histórico de Toledo',see_rooms='Ver las habitaciones',hero_k='Toledo · C/ Santa Isabel 24',hero_t='Las vistas de Toledo, desde nuestra terraza',hero_s='Un hotel en una antigua casa noble del corazón del casco histórico.',
 intro_t='Una casa noble toledana',intro_p1='El Hotel Santa Isabel abrió en 1990 en pleno casco histórico, la ciudad amurallada que abraza el río Tajo, a pocos pasos de la Catedral.',
 intro_p2='Conserva balcones originales de la antigua casa noble y techos de madera que estuvieron ocultos durante años, algunos con la pintura de los escudos de las familias que vivieron aquí en el siglo XV.',
 stats=['Abierto en 1990','Recepción 24 h','Terraza panorámica','Garaje bajo petición'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Todas con aire acondicionado o calefacción, TV, teléfono, wifi y aseo con ducha.',
 svcs=['Recepción 24 h','Terraza panorámica','Cafetería en horario de desayuno','Garaje bajo petición','Guardaequipajes','Ascensores'],
 around_s='La Catedral, la Plaza de Zocodover, el Alcázar, Santo Tomé y San Juan de los Reyes, todo a pie desde el casco histórico.',
 loc_p='C/ Santa Isabel 24 · 45002 Toledo, en el casco histórico. Recepción abierta las 24 horas.',
 chips=['¿Qué habitaciones tenéis?','¿Hay desayuno?','¿Dónde aparco?','¿Cómo reservo?']),
'en':dict(title='Hotel Santa Isabel · Family hotel in Toledo’s historic centre',see_rooms='See the rooms',hero_k='Toledo · C/ Santa Isabel 24',hero_t='Toledo’s views, from our terrace',hero_s='A hotel in a former noble house in the heart of the old town.',
 intro_t='A Toledo noble house',intro_p1='Hotel Santa Isabel opened in 1990 in the heart of the old town, the walled city wrapped by the river Tagus, a few steps from the Cathedral.',
 intro_p2='It keeps original balconies from the old noble house and wooden ceilings hidden for years, some still painted with the coats of arms of the families who lived here in the 15th century.',
 stats=['Open since 1990','24-hour reception','Panoramic terrace','Garage on request'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='All with air conditioning or heating, TV, telephone, wifi and shower room.',
 svcs=['24-hour reception','Panoramic terrace','Café at breakfast time','Garage on request','Luggage storage','Lifts'],
 around_s='The Cathedral, Plaza de Zocodover, the Alcázar, Santo Tomé and San Juan de los Reyes, all on foot from the old town.',
 loc_p='C/ Santa Isabel 24 · 45002 Toledo, in the historic centre. Reception open 24 hours.',
 chips=['Which rooms do you have?','Is there breakfast?','Where can I park?','How do I book?']),
'fr':dict(title='Hôtel Santa Isabel · Hôtel familial dans le centre historique de Tolède',see_rooms='Voir les chambres',hero_k='Tolède · C/ Santa Isabel 24',hero_t='Les vues de Tolède, depuis notre terrasse',hero_s='Un hôtel dans une ancienne maison noble au cœur de la vieille ville.',
 intro_t='Une maison noble tolédane',intro_p1='L’Hôtel Santa Isabel a ouvert en 1990 en plein centre historique, la ville fortifiée qu’enlace le Tage, à quelques pas de la cathédrale.',
 intro_p2='Il conserve des balcons d’origine de l’ancienne maison noble et des plafonds en bois longtemps cachés, certains encore peints des blasons des familles qui y vécurent au XVe siècle.',
 stats=['Ouvert en 1990','Réception 24 h/24','Terrasse panoramique','Garage sur demande'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Toutes avec climatisation ou chauffage, TV, téléphone, wifi et salle d’eau avec douche.',
 svcs=['Réception 24 h/24','Terrasse panoramique','Cafétéria à l’heure du petit-déjeuner','Garage sur demande','Bagagerie','Ascenseurs'],
 around_s='La cathédrale, la Plaza de Zocodover, l’Alcázar, Santo Tomé et San Juan de los Reyes, tout à pied depuis la vieille ville.',
 loc_p='C/ Santa Isabel 24 · 45002 Tolède, dans le centre historique. Réception ouverte 24 h/24.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un petit-déjeuner ?','Où me garer ?','Comment réserver ?']),
'de':dict(title='Hotel Santa Isabel · Familienhotel in der Altstadt von Toledo',see_rooms='Zimmer ansehen',hero_k='Toledo · C/ Santa Isabel 24',hero_t='Toledos Aussicht, von unserer Terrasse',hero_s='Ein Hotel in einem ehemaligen Adelshaus im Herzen der Altstadt.',
 intro_t='Ein toledanisches Adelshaus',intro_p1='Das Hotel Santa Isabel öffnete 1990 mitten in der Altstadt, der vom Tajo umschlossenen ummauerten Stadt, wenige Schritte von der Kathedrale.',
 intro_p2='Es bewahrt originale Balkone des alten Adelshauses und lange verborgene Holzdecken, teils noch mit den Wappen der Familien, die hier im 15. Jahrhundert lebten.',
 stats=['Seit 1990','Rezeption rund um die Uhr','Panoramaterrasse','Garage auf Anfrage'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Alle mit Klimaanlage oder Heizung, TV, Telefon, WLAN und Duschbad.',
 svcs=['Rezeption rund um die Uhr','Panoramaterrasse','Cafeteria zur Frühstückszeit','Garage auf Anfrage','Gepäckaufbewahrung','Aufzüge'],
 around_s='Kathedrale, Plaza de Zocodover, Alcázar, Santo Tomé und San Juan de los Reyes, alles zu Fuß aus der Altstadt.',
 loc_p='C/ Santa Isabel 24 · 45002 Toledo, in der Altstadt. Rezeption rund um die Uhr geöffnet.',
 chips=['Welche Zimmer gibt es?','Gibt es Frühstück?','Wo kann ich parken?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://reservas.datahotel.net/Reservar/hotelsantaisabeltoledo.es/'
BOOK=dict(mode='engine',url=dict(es=R+'es',en=R+'en',fr=R+'fr-FR',de=R+'de-DE'))
D=dict(name='Hotel Santa Isabel',ac='#1f2a36',ac2='#8a5a2e',ac2_a11y='#6e4622',book=BOOK,around=['Catedral de Toledo','Plaza de Zocodover'],foot=FOOT,
 address='C/ Santa Isabel 24 · 45002 Toledo',phones=['+34 925 25 31 20'],emails=['info@hotelsantaisabeltoledo.es'],maps='Hotel Santa Isabel, Calle Santa Isabel 24, 45002 Toledo',t=T)
META=dict(repo='demo-hotel-santa-isabel-toledo',name='Hotel Santa Isabel',legal_name='Hotel El Tropezón S.L. (aviso legal de su web)',registry_ids=['B45044161'],
 url='https://hotelsantaisabeltoledo.es/es/',domain='hotelsantaisabeltoledo.es',municipality='Toledo',province='Toledo',sector='hotel familiar en una antigua casa noble del casco histórico de Toledo',
 read_at='2026-10-30T11:17:00+01:00',created_at='2026-10-30T11:16:00+01:00',built_at='2026-10-30T11:30:00+01:00',audit_date='2026-10-30T11:08:54+01:00',
 rating=dict(value=4.5,coincide=['tel', 'web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Santa+Isabel/@39.8555112,-4.0250482,17z/data=!4m9!3m8!1s0xd6a0ba6c9ae780f:0xd40885418117c1aa!5m2!4m1!1i2!8m2!3d39.8555112!4d-4.0250482!16s%2Fg%2F1vzv4_t3'),
 book=dict(mode='engine',url=R+'es',note='motor de reservas real enlazado desde su web (Datahotel), HTTP 200 comprobado el 30/10/2026 en /es, /en, /fr-FR y /de-DE.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay desayuno?','K02'),('¿Dónde aparco?','K03'),('¿Tenéis cuna para bebés?','K04'),('¿Se puede fumar?','K05'),('¿Dónde está el hotel?','K06'),('¿Qué hay cerca?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay terraza?','K09'),('¿Hay recepción 24 horas?','K10'),('¿Hay wifi?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Is there breakfast?','K02'),('Where can I park?','K03'),('Do you have a cot for babies?','K04'),('Can I smoke?','K05'),('Where is the hotel?','K06'),('What is nearby?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there a terrace?','K09'),('Is reception open 24 hours?','K10'),('Is there wifi?','K11'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il un petit-déjeuner ?','K02'),('Où me garer ?','K03'),('Avez-vous un lit bébé ?','K04'),('Peut-on fumer ?','K05'),('Où se trouve l’hôtel ?','K06'),('Qu’y a-t-il à proximité ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il une terrasse ?','K09'),('La réception est-elle ouverte 24 h/24 ?','K10'),('Y a-t-il le wifi ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es Frühstück?','K02'),('Wo kann ich parken?','K03'),('Gibt es ein Babybett?','K04'),('Darf man rauchen?','K05'),('Wo liegt das Hotel?','K06'),('Was gibt es in der Nähe?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es eine Terrasse?','K09'),('Ist die Rezeption rund um die Uhr besetzt?','K10'),('Gibt es WLAN?','K11'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
