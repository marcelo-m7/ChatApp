map.MapConfiguration(    interaction_configuration=map.MapInteractionConfiguration(        flags=map.MapInteractiveFlag.PINCH_ZOOM | map.MapInteractiveFlag.ROTATE    ))

map.MapConfiguration(    interaction_configuration=map.MapInteractionConfiguration(        flags=map.MapInteractiveFlag.ALL & ~map.MapInteractiveFlag.ROTATE    ))

