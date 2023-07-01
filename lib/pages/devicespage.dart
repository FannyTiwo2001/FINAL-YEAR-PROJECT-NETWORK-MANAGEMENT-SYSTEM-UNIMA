import 'package:flutter/material.dart';
import 'package:netmanmain/components/devicestile.dart';
import 'package:netmanmain/data/device_group_data.dart';
import 'package:provider/provider.dart';

class DeviceView extends StatefulWidget {
  final String myIPAddress;
  final String deviceGroupName;

  const DeviceView({
    super.key, required this.myIPAddress, required this.deviceGroupName,
    // required this.deviceGroupName,
  });

  @override
  State<DeviceView> createState() => _DeviceViewState();
}

class _DeviceViewState extends State<DeviceView> {
  // const DeviceView({super.key, required this.ipAddress});
  @override
  Widget build(BuildContext context) {
    return Consumer<DeviceGroupData>(
      builder: (context, value, child) => MaterialApp(
        debugShowCheckedModeBanner: false,
        home: Scaffold(
          appBar: AppBar(
            leading: IconButton(
                onPressed: () {
                  Navigator.pop(context);

                },
                icon: const Icon(
                  Icons.arrow_back,
                )),
            title: const Text("Routers"),
            titleSpacing: 90,
          ),
          body: Container(
            height: double.infinity,
            color: Colors.grey[300],
            padding: const EdgeInsets.all(10),
            child: ListView.builder(
                itemCount: value.numberOfDevicesInGroup(widget.deviceGroupName),
                shrinkWrap: true,
                itemBuilder: (context, index) {
                  return DeviceTile(deviceIpAddress: widget.myIPAddress,);
                }),
          ),
        ),
      ),
    );
  }
}
