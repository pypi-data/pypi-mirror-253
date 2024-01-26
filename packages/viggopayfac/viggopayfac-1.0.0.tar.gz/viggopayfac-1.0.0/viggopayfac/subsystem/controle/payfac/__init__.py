from viggocore.common import subsystem
from viggopayfac.subsystem.controle.payfac \
  import resource, controller, router, manager

subsystem = subsystem.Subsystem(resource=resource.NuvemFiscal,
                                controller=controller.Controller,
                                manager=manager.Manager,
                                router=router.Router)
