from abstract_factory import ModernFactory


modern_factory = ModernFactory()

modern_chair = modern_factory.create_chair()

print(modern_chair)
