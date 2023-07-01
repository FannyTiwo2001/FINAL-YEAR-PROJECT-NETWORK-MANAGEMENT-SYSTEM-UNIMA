import 'package:flutter/material.dart';
import 'package:netmanmain/data/device_group_data.dart';
import 'package:provider/provider.dart';


class DeviceCardView extends StatefulWidget {
  final List<String> images;
  final List<String> names;
  final String groupName;
  const DeviceCardView({super.key, required this.images, required this.names, required this.groupName});

  @override
  State<DeviceCardView> createState() => _DeviceCardViewState();
}


class _DeviceCardViewState extends State<DeviceCardView> {
  @override
  Widget build(BuildContext context) {
    return Consumer<DeviceGroupData>(
      builder: (context, value, child) => Container(
        width: 150,
        height: 300,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(15),
          boxShadow: [
            BoxShadow(
              color: Colors.grey.withOpacity(0.5),
              spreadRadius: 3,
              blurRadius: 10,
              offset: const Offset(0, 3),
            )
          ],
        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 5),
          child: Column(
            children: [
              for (String img in widget.images)
                Image.asset(img, height: 75, width: 50,),
              for(String name in widget.names)
                Text(name, style: const TextStyle(fontSize: 23, fontWeight: FontWeight.bold),),
              const SizedBox(height: 15,),
              const Text("0", style: TextStyle(fontSize: 16, ),),
            ],
          ),
        ),
      ),
    );
  }
}
