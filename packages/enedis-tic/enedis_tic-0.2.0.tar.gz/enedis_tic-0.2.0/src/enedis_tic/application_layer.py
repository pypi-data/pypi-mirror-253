from collections import namedtuple
import json
import os


_PACKAGE_PATH = os.path.dirname(__file__)
with open(os.path.join(_PACKAGE_PATH, 'infos.json'), 'r') as f:
    infos = json.loads(f.read())
with open(os.path.join(_PACKAGE_PATH, 'euridis.json'), 'r') as f:
    euridis = json.loads(f.read())


Measure = namedtuple('Measure', ('value', 'unit'))
HorodateMeasure = namedtuple('HorodateMeasure', ('value', 'unit', 'datetime'))


class FrameParser:
    def __init__(self, frame):
        self.frame = frame

    def to_dict(self):
        res = dict()
        for key, value in self.frame.items():
            try:
                res.update(getattr(self, f'_parse_{key.lower()}')(value['data']))
            except AttributeError:
                res.update(self._info(key, value))
        return res

    @staticmethod
    def _info(key, value):
        try:
            info = infos[key]
            try:
                unit = info['unit']
                if unit == 'datetime':
                    return {info['name']: Measure(value['datetime'], unit)}
                elif value['datetime']:
                    return {info['name']: HorodateMeasure(int(value['data']), unit, value['datetime'])}
                return {info['name']: Measure(int(value['data']), unit)}
            except KeyError:
                return {info['name']: value['data']}
        except KeyError:
            return {key: value['data']}

    @staticmethod
    def _parse_adsc(value):
        datas = dict()
        datas['Adresse secondaire du compteur'] = value
        datas['Constructeur'] = euridis['constructeurs'].get(value[0:2], None)
        try:
            datas['Année de fabrication'] = 2000 + int(value[2:4])
        except ValueError:
            pass
        datas['Appareil'] = euridis['appareils'].get(value[4:6], None)
        datas['Numéro de série'] = value[6:]
        return datas

    @staticmethod
    def _parse_optarif(value):
        if value.startswith('BBR'):
            option = 'Tempo'
        else:
            option = {
                'BASE': 'Base',
                'HC..': 'Heures Creuses',
                'EJP.': 'EJP'
            }.get(value, value)
        return {'Option tarifaire choisie': option}

    @staticmethod
    def _parse_stge(value):
        value = int(value, base=16)

        return {
            'Contact sec': ['fermé', 'ouvert'][_get_bit_int(value, index=0)],
            'Organe de coupure': ['fermé', 'ouvert sur surpuissance', 'ouvert sur surtension', 'ouvert sur délestage', 'ouvert sur ordre CPL ou Euridis', 'ouvert sur une surchauffe avec une valeur du courant supérieure au courant de commutation maximal', 'ouvert sur une surchauffe avec une valeur de courant inférieure au courant de commutation maximal'][_get_bit_int(value, index=1, length=3)],
            'État du cache-bornes distributeur': ['fermé', 'ouvert'][_get_bit_int(value, index=4)],
            'Surtension sur une des phases': ['pas de surtension', 'surtension'][_get_bit_int(value, index=6)],
            'Dépassement de la puissance de référence': ['pas de dépassement', 'dépassement en cours'][_get_bit_int(value, index=7)],
            'Fonctionnement producteur/consommateur': ['consommateur', 'producteur'][_get_bit_int(value, index=8)],
            'Sens de l’énergie active': ['énergie active positive', 'énergie active négative'][_get_bit_int(value, index=9)],
            'Tarif en cours sur le contrat fourniture': 'énergie ventilée sur Index {}'.format(_get_bit_int(value, index=10, length=3) + 1),
            'Tarif en cours sur le contrat distributeur': 'énergie ventilée sur Index {}'.format(_get_bit_int(value, index=14, length=2) + 1),
            'Mode dégradée de l’horloge (perte de l’horodate de l’horloge interne)': ['horloge correcte', 'horloge en mode dégradée'][_get_bit_int(value, index=16)],
            'État de la sortie télé-information': ['mode historique', 'mode standard'][_get_bit_int(value, index=17)],
            'État de la sortie communication Euridis': ['désactivée', 'activée sans sécurité', '', 'activée avec sécurité'][_get_bit_int(value, index=19, length=2)],
            'Statut du CPL':  ['New/Unlock', 'New/Lock', 'Registered'][_get_bit_int(value, index=21, length=2)],
            'Synchronisation CPL': ['compteur non synchronisé', 'compteur synchronisé'][_get_bit_int(value, index=23)],
            'Couleur du jour pour le contrat historique tempo': ['Pas d‘annonce', 'Bleu', 'Blanc', 'Rouge'][_get_bit_int(value, index=24, length=2)],
            'Couleur du lendemain pour le contrat historique tempo': ['Pas d‘annonce', 'Bleu', 'Blanc', 'Rouge'][_get_bit_int(value, index=26, length=2)],
            'Préavis pointes mobiles': ['pas de préavis en cours', 'préavis PM1 en cours', 'préavis PM2 en cours', 'préavis PM3 en cours'][_get_bit_int(value, index=28, length=2)],
            'Pointe mobile (PM)': ['Pas de pointe mobile', 'PM 1 en cours', 'PM 2 en cours', 'PM 3 en cours'][_get_bit_int(value, index=30, length=2)]
        }

    @staticmethod
    def _parse_relais(value):
        value = int(value, base=10)
        return {'Relai {}'.format(i + 1): ['ouvert', 'fermé'][_get_bit_int(value, index=i)] for i in range(8)}


def _get_bit_int(val, index, length=1):
    return int((val >> index) & ((2**length)-1))
