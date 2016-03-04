using System;
using System.Reflection;
using System.Runtime.InteropServices;
using Appst.IO.Serial.Interfaces;

namespace Appst.IO.Serial {
    public class Platform {

        /// <summary> Gets the default controller for a given platform. </summary>
        /// <returns> The serial port controller. </returns>
        public static ISerialController GetController() {
            ISerialController ret = null;
            bool IsWindows = true;
            // TODO Test if Windows, I think this is currenty a bug in CoreFx
            //IsWindows = RuntimeInformation.IsOSPlatform(OSPlatform.Windows);
           
            if (IsWindows) {
                // Get the Windows Controller
                var wincontroller = Type.GetType("Appst.IO.Serial.Win32.SerialController, Appst.IO.Serial.Win32");
                if (wincontroller != null)
                    ret = (ISerialController) wincontroller.GetMethod("GetDefault").Invoke(null, null);
            }
            else {
                // Get the Linux Controller
                var wincontroller = Type.GetType("Appst.IO.Serial.LinuxMono.SerialController, Appst.IO.Serial.LinuxMono");
                if (wincontroller != null)
                    ret = (ISerialController)wincontroller.GetMethod("GetDefault").Invoke(null, null);
            }
            return ret;
        }
    }
}