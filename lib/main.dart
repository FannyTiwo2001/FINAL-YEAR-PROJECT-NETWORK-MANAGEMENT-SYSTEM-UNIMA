import 'package:flutter/material.dart';
import 'package:netmanmain/data/device_group_data.dart';
import 'package:netmanmain/pages/homepage.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(const NetMan());
}

class NetMan extends StatelessWidget {
  const NetMan({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => DeviceGroupData(),
      child: const MaterialApp(
        debugShowCheckedModeBanner: false,
        home: HomePage(),
      ),
    );
  }
}
