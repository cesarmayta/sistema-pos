from rest_framework import serializers

from .models import(
    Mesa,Categoria,Plato,Pedido,PedidoPlato
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields =  '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation
        
class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation
        
class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['plato_img'] = instance.plato_img.url
        return representation
    
class CategoriaPlatoSerializer(serializers.ModelSerializer):
    Platos = PlatoSerializer(many=True,read_only=True)
    
    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nom','Platos'] 
        
""" serializers para registro de pedido """
class PedidoPlatoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fiedls = '__all__'
        
class PedidoSerializerPOST(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerPOST(many=True)
    
    class Meta:
        model = Pedido
        fields = ['pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos']
        
    def create(self,validated_data):
        lista_pedido_platos = validated_data.pop('pedidoplatos')
        print(lista_pedido_platos)
        pedido = Pedido.objects.create(**validated_data)
        print(pedido.pedido_id)
        for obj_pedido_plato in lista_pedido_platos:
            PedidoPlato.objects.create(pedido_id=pedido,**obj_pedido_plato)
        return pedido