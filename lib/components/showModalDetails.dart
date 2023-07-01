import 'package:flutter/material.dart';
import 'package:netmanmain/data/device_group_data.dart';
import 'package:provider/provider.dart';

class MoreDeviceDetails extends StatefulWidget {
  final String deviceName;
  final String memory;
  final String usedMemory;
  final String cpu;
  final String location;

  const MoreDeviceDetails(
      {super.key,
      required this.deviceName,
      required this.memory,
      required this.usedMemory,
      required this.cpu,
      required this.location});

  @override
  State<MoreDeviceDetails> createState() => _MoreDeviceDetailsState();
}

class _MoreDeviceDetailsState extends State<MoreDeviceDetails> {
  @override
  Widget build(BuildContext context) {
    return Consumer<DeviceGroupData>(
      builder: (context, value, child) => GestureDetector(
        onTap: () {
          //execute bottom modal sheet function
          showModalBottomSheet(
            context: context,
            // isDismissible: false,
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.only(
                  topRight: Radius.circular(20), topLeft: Radius.circular(20)),
            ),
            builder: ((context) {
              return ListView(
                children: [
                  ListTile(
                    leading: const Text(
                      "Name : ",
                      style: TextStyle(fontSize: 20),
                    ),
                    trailing: Text(widget.deviceName,
                        style: const TextStyle(fontSize: 20)),
                  ),
                  ListTile(
                    leading: const Text(
                      "Total Memory (RAM): ",
                      style: TextStyle(fontSize: 20),
                    ),
                    trailing: Text(widget.memory,
                        style: const TextStyle(fontSize: 20)),
                  ),
                  ListTile(
                    leading: const Text(
                      "Memory in Use: ",
                      style: TextStyle(fontSize: 20),
                    ),
                    trailing: Text(widget.usedMemory,
                        style: const TextStyle(fontSize: 20)),
                  ),
                  ListTile(
                    leading: const Text(
                      "CPU : ",
                      style: TextStyle(fontSize: 20),
                    ),
                    trailing:
                        Text(widget.cpu, style: const TextStyle(fontSize: 20)),
                  ),
                  ListTile(
                    leading: const Text(
                      "Location : ",
                      style: TextStyle(fontSize: 20),
                    ),
                    trailing: Text(widget.location,
                        style: const TextStyle(fontSize: 20)),
                  ),
                ],
              );
            }),
          );
        },
      ),
    );
  }
}
