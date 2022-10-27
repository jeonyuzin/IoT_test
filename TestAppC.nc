configuration TestAppC
{
}
implementation{
        components MainC, TestC, LedsC;
        TestC -> MainC.Boot;
        TestC.Leds -> LedsC;

        components PlatformSerialC;
        TestC.SerialControl -> PlatformSerialC;
        TestC.UartByte -> PlatformSerialC;
        TestC.UartStream -> PlatformSerialC;

        //components ActiveMessageC, new AMSenderC(AM_OSCILLOSCOPE);
        components ActiveMessageC, new AMSenderC(0x94);
        TestC.RadioControl -> ActiveMessageC;
        TestC.AMSend -> AMSenderC;
}

