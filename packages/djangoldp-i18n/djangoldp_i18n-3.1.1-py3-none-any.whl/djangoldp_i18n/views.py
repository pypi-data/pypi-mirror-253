from djangoldp.views import LDPViewSet
from djangoldp_i18n.serializers import I18nLDPSerializer, I18nContainerSerializer


class I18nLDPViewSet(LDPViewSet):
    '''
    Overrides LDPViewSet to use custom serializer
    '''
    serializer_class = I18nLDPSerializer