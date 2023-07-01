import 'package:flutter/material.dart';

import '../models/interfaces.dart';

class DeviceTile extends StatefulWidget {
  final String deviceIpAddress;

  const DeviceTile({super.key, required this.deviceIpAddress});

  // final String deviceName;
  // final String memory;
  // final String usedMemory;
  // final String cpu;
  // final String location;

  // final List<Interfaces> interfaces;

  // const DeviceTile({
  //   super.key,
  //   required this.deviceName,
  //   required this.memory,
  //   required this.usedMemory,
  //   required this.cpu,
  //   required this.location,
  //   // required this.interfaces
  // });

  @override
  State<DeviceTile> createState() => _DeviceTileState();
}

class _DeviceTileState extends State<DeviceTile> {
  bool isSelected = false;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(
        top: 20,
      ),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20.0),
        color: Colors.indigo,
      ),
      child: GestureDetector(
        onTap: () {},
        child: ListTile(
          leading: const Icon(
            Icons.router_rounded,
            size: 35.0,
          ),
          title: Text(widget.deviceIpAddress),
          // subtitle: const Text("192.168.12.1"),
          trailing: Switch(
            value: isSelected,
            onChanged: (value) {
              setState(() {
                isSelected = !isSelected;
              });
            },
            activeColor: Colors.green,
          ),
          iconColor: Colors.white,
          textColor: Colors.white,
        ),
      ),
    );
  }
}
