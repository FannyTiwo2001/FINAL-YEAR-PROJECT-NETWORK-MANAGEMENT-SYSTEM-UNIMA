import 'package:netmanmain/models/devices.dart';
import 'package:netmanmain/models/interfaces.dart';

class Routers extends Device {
  // final List<Interfaces> interfacesList;

  Routers({
    required super.deviceName,
    required super.memory,
    required super.usedMemory,
    required super.cpu,
    required super.location,
    // required this.interfacesList,
  });
}
