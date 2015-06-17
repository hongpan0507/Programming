// $Id: jpcap.c,v 1.24 2004/10/07 18:04:41 pcharles Exp $

/***************************************************************************
 * Copyright (C) 2001, Patrick Charles and Jonas Lehmann                   *
 * Distributed under the Mozilla Public License                            *
 *   http://www.mozilla.org/NPL/MPL-1.1.txt                                *
 ***************************************************************************/

// A libpcap wrapper with java native hooks.
//
// @author Jonas Lehmann and Patrick Charles
// @version $Revision: 1.24 $
// @lastModifiedBy $Author: pcharles $
// @lastModifiedAt $Date: 2004/10/07 18:04:41 $
//
#include <stdio.h>
#include <stdlib.h>
extern "C" {
#include <pcap.h>
}
#include <JavaVM/jni.h>
#include "process.hpp"


#ifndef WIN32
#include <errno.h>
#include <string.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <unistd.h>
#else /*WIN32*/

/* KRIS: (28/04/2002) It seems to me that __int64 is a CygWin GCC problem
   MSVC has __int64 as a build type */
#ifdef	__GNUC__
//  typedef long __int64;
//  /* FIXME: This is dirty.            */
//  /* __int64 required for jlong in jni_md.h */
//  /* __int64 should be 8 byte integer         */

#endif

#endif /*WIN32*/

// native function headers generated by javah
#include "net_sourceforge_jpcap_capture_PacketCapture.h"

#if !defined(__FreeBSD__) && !defined(__NetBSD__) && !defined(__OpenBSD__) && \
    !defined(__bsdi__) && !defined(__APPLE__) && !defined(WIN32) && \
    !defined(__CYGWIN__)
# define DO_SELECT
#endif


/*****************************************************************************
 * global variables 
 */

#define FALSE 0
#define TRUE 1

static pcap_t *PD[10] = // packet capture device.
  {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL}; 
jobject javaObject; // reference to java object hooked into this wrapper lib.
JNIEnv *javaEnvironment; // java vm containing running java object.
const int VERBOSE = 0; // for debugging

typedef struct pcap_attr {
  int pcapGo;
  // add any further attributes here.
};

/*
static int pcapGo[10] = // state variable for each packet capture device
  {FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE};
*/

static pcap_attr attr[10] = // state variable for each packet capture device
  {{0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}};

const char *DEVICE_NOT_FOUND_EXCEPTION = 
  "net/sourceforge/jpcap/capture/CaptureDeviceNotFoundException";
const char *DEVICE_OPEN_EXCEPTION = 
  "net/sourceforge/jpcap/capture/CaptureDeviceOpenException";
const char *DEVICE_LOOKUP_EXCEPTION = 
  "net/sourceforge/jpcap/capture/CaptureDeviceLookupException";
const char *CAPTURE_EXCEPTION = 
  "net/sourceforge/jpcap/capture/CapturePacketException";
const char *CONFIGURATION_EXCEPTION = 
  "net/sourceforge/jpcap/capture/CaptureConfigurationException";
const char *INVALID_FILTER_EXCEPTION = 
  "net/sourceforge/jpcap/capture/InvalidFilterException";
const char *CLASS_EXCEPTION = 
  "java/lang/ClassNotFoundException";
const char *FILE_OPEN_EXCEPTION = 
  "net/sourceforge/jpcap/capture/CaptureFileOpenException";


/*****************************************************************************
 * utility functions
 */

/*
 * Write captured packet data to stderr.
 */
void printPacket(u_char *user, u_char *cp, u_int caplen, u_int length, 
                 u_int seconds, u_int useconds)
{
  register u_int i, s;
  register int nshorts;

  nshorts = (u_int) caplen / sizeof(u_short);

  fprintf(stderr, "Packet: u = %s, l = %d of %d, t = %u.%06u, d = ", 
          user, caplen, length, seconds, useconds);

  i = 0;
  while (--nshorts >= 0) {
    if ((i++ % 8) == 0)
      fprintf(stderr, "\n\t\t\t");
    s = *cp++;
    fprintf(stderr, " %02x%02x", s, *cp++);
  }

  if (caplen & 1) {
    if ((i % 8) == 0)
      (void)fprintf(stderr, "\n\t\t\t");
    (void)fprintf(stderr, " %02x", *cp);
  }

  fprintf(stderr, "\t\n");
}


/*
 * Create and throw an exception into the Java VM using this wrapper.
 * If the specified exception class can't be found, the VM will throw
 * a class not found exception.
 */
void throwException(JNIEnv *env, const char *excClassName, char *message) {
  // create an instance of the specified exception
  jclass exception = env->FindClass(excClassName);

  if(exception != NULL) 
    // throw the new exception back to the java wrapper
    env->ThrowNew(exception, message);

  // free the local reference. if exception is still null, delete is a noop.
  env->DeleteLocalRef(exception);

}


/*****************************************************************************
 * implementation of pcap wrapper functions with java hooks
 */

/*
 * Callback called by pcap_loop() for processing packet data.
 * This method is called whenever a packet is captured by the pcap_loop()
 * in _capture(). It decomposes the captured data and transfers it 
 * to the PacketCapture object in the attached java VM.
 */
void processData(u_char *user, struct pcap_pkthdr *h, jbyte *sp) {
  processing *proc;
  proc = (processing *) user;
  proc->processData(user, h, sp);
}

/*
 * Look up a network device.
 * Throws a CaptureDeviceNotFoundException if no suitable device is found.
 *
 * JNI PacketCapture.findDevice()
 */
JNIEXPORT jstring JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_findDevice
(JNIEnv *env, jobject obj) {
  char ebuf[PCAP_ERRBUF_SIZE];

#ifndef WIN32
  char *device = pcap_lookupdev(ebuf);

  if(device == NULL) {
    // if no device can be found, throw an exception back to the java wrapper
    throwException(env, DEVICE_NOT_FOUND_EXCEPTION, ebuf);
    return NULL;
  }
  else 
    return env->NewStringUTF(device);

#else /*WIN32*/
  //char buf[256]; 
  wchar_t *dev;
  char buf_all[516];
  char* desc = 0;
  int i=0, t=0;
  dev = (wchar_t *)pcap_lookupdev(ebuf);
  if (dev) {
    if (dev[0]<256) { /* NT / 2000 */
      if (dev[0]==0 && dev[1]==0) {
        throwException(env, DEVICE_NOT_FOUND_EXCEPTION, ebuf);
        return NULL; /* no device */
      }
      // Do the same thing as lookupDevices, so that we can
      // find a human-readable device name
      //wcstombs(buf,(wchar_t *)dev,255);
      //return env->NewStringUTF(buf);

      while(!(dev[i]==0 && dev[i-1]==0)) {
        i++;
      }

      // human-readable descriptions are placed after the device names
      desc = (char*)(dev + i + 1);

      t = wcstombs(buf_all,(wchar_t *)dev,255);

      buf_all[t++] = '\n';
      buf_all[t++] = ' ';
      buf_all[t++] = ' '; // set "\n  " as windows signature

      while (*desc != 0) {
        if (t < 514)
          buf_all[t++] = *desc;
        desc++;
      }
      return env->NewStringUTF(buf_all);

    } else { /* 9x */
      char *dev9x = (char *)dev;

      if (dev9x[0]==0 && dev9x[1]==0) {
        throwException(env, DEVICE_NOT_FOUND_EXCEPTION, ebuf);
        return NULL; /* no device */
      }

      return env->NewStringUTF((char *)(dev9x));
    }
  } else {
    throwException(env, DEVICE_NOT_FOUND_EXCEPTION, ebuf);
    return NULL; /* no device */
  }

#endif
}

/*
 * Open a network device for data capture.
 * Throws an OpenException if the device cannot be opened.
 * If the open is successful, sets the global device pointer.
 *
 * JNI PacketCapture.open()
 */
JNIEXPORT void JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_open
  (JNIEnv *env, jobject object, jint instance, jstring jdevice, jint snaplen,
   jboolean promiscuous, jint timeout)
{
  char ebuf[PCAP_ERRBUF_SIZE];
  int linkType;
  jfieldID fid;
  jclass cls;
  const char *device;

  if(jdevice == NULL) {
    // device can't be null; throw an exception back to java wrapper
    throwException(env, DEVICE_OPEN_EXCEPTION, "null device specified");
    return;
  }

  device = env->GetStringUTFChars(jdevice, 0);

  PD[instance] = 
    pcap_open_live((char*)device, snaplen, promiscuous, timeout, ebuf);

  if(PD[instance] == NULL) {
    // if the open fails, throw an exception back to the java wrapper
    throwException(env, DEVICE_OPEN_EXCEPTION, ebuf);
    return;
  }

  attr[instance].pcapGo = FALSE;

  // set the link type in the java wrapper encapsulating the capture system
  linkType = pcap_datalink(PD[instance]);
  cls = env->GetObjectClass(object);
  fid = env->GetFieldID(cls, "linkType", "I");

  if (fid == 0) {
    // catch native/java field inconsistencies
    throwException(env, CLASS_EXCEPTION,
		   "couldn't find member PacketCapture.linkType!");
    return;
  }
  env->SetIntField(object, fid, linkType);
}

/*
 * Open a tcpdump-formatted "savefile" for reading captured packets 
 * as an alternative to capturing packets off the wire.
 *
 * JNI PacketCapture.openOffline()
 */
JNIEXPORT void JNICALL
Java_net_sourceforge_jpcap_capture_PacketCapture_openOffline
  (JNIEnv *env, jobject object, jint instance, jstring jfileName)
{
  const char* fileName;
  char ebuf[PCAP_ERRBUF_SIZE];
  jfieldID fid;
  jclass cls;
  int linkType;

  if(jfileName == NULL) {
    throwException(env, FILE_OPEN_EXCEPTION, "null file name specified" );
    return;
  }

  fileName = env->GetStringUTFChars(jfileName, 0);
  PD[instance] = pcap_open_offline(fileName, ebuf);

  if(PD[instance] == NULL) {
    throwException(env, FILE_OPEN_EXCEPTION, ebuf);
    return;
  }

  // set the link type in the java wrapper encapsulating the capture system
  linkType = pcap_datalink(PD[instance]);
  cls = env->GetObjectClass(object);
  fid = env->GetFieldID(cls, "linkType", "I");
  if (fid == 0) {
    // catch native/java field inconsistencies
    throwException(env, CLASS_EXCEPTION, 
                   "couldn't find member PacketCapture.linkType!");
    return;
  }
  env->SetIntField(object, fid, linkType);

  attr[instance].pcapGo = FALSE;

}

/*
 * Capture packets.
 * Throws a CapturePacketException if a problem occurs during the capture.
 *
 * JNI PacketCapture.capture()
 */
JNIEXPORT void JNICALL Java_net_sourceforge_jpcap_capture_PacketCapture_capture 
(JNIEnv *env, jobject obj, jint instance, jint count) {

  processing *p = new(processing);
  p->javaEnvironment = env;
  p->javaObject = obj;

  // make sure a device is open before allowing the capture session to start
  if(PD[instance] == NULL) {
    throwException(env, CAPTURE_EXCEPTION,
                   "a device must be open before capturing packets");
    return;
  }

#ifdef PCAP_LOOP  // the old way of capturing
  if (pcap_loop(PD[instance], count,
		(pcap_handler)processData, (u_char *)p) < 0)
  // if the capture failed, throw an exception back to the java wrapper
  throwException(env, CAPTURE_EXCEPTION, pcap_geterr(PD[instance]));

#else
  attr[instance].pcapGo = TRUE;
  int cnt = 0;
  if (pcap_file(PD[instance]) == NULL) { // live capture

#ifdef DO_SELECT
    fd_set fd_wait;
    int sel;
    struct timeval st;

    while (attr[instance].pcapGo && ((count <= 0) ? true : (cnt < count)))
    {
      FD_ZERO(&fd_wait);
      FD_SET(pcap_fileno(PD[instance]), &fd_wait);
      st.tv_sec	 = 1;
      st.tv_usec = 0;

      sel = select(FD_SETSIZE, &fd_wait, NULL, NULL, &st);

      if (sel > 0) { // OK, select says we have a packet in the queue
	cnt++;
	if (pcap_dispatch(PD[instance], 1,
                          (pcap_handler)processData, (u_char *)p) < 0) {
          // if the capture failed, throw an exception back to the java wrapper
	  throwException(env, CAPTURE_EXCEPTION, pcap_geterr(PD[instance]));
	  return;
	}
      } else if (sel < 0) {
	throwException(env, CAPTURE_EXCEPTION, "select() returns -1");
	return;
      }
    }

#else // !DO_SELECT
    while (attr[instance].pcapGo && ((count <= 0) ? true : (cnt < count))) {
      cnt++;
      if (pcap_dispatch(PD[instance], 1,
                        (pcap_handler)processData, (u_char *)p) < 0) {
        // if the capture failed, throw an exception back to the java wrapper
	throwException(env, CAPTURE_EXCEPTION, pcap_geterr(PD[instance]));
	return;
      }
    }

#endif // DO_SELECT
  } 
  else {
    while (attr[instance].pcapGo && ((count <= 0) ? true : (cnt < count))) {
      cnt++;
      int ret = (pcap_dispatch(PD[instance], 1,
                               (pcap_handler)processData, (u_char *)p));
      if (ret < 0) {
        // if the capture failed, throw an exception back to the java wrapper
	throwException(env, CAPTURE_EXCEPTION, pcap_geterr(PD[instance]));
	return;
      } else if (ret == 0) {
	attr[instance].pcapGo = FALSE; // end of savefile
      }
    }
  }

#endif	// PCAP_LOOP
}

/*
 * Stop capturing packets
 *
 * JNI PacketCapture.endCapture()
 */
JNIEXPORT void JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_endCapture
(JNIEnv *env, jobject obj, jint instance) {
  attr[instance].pcapGo = FALSE;
}

/*
 * Fetch the network associated with the device.
 * Throws a CaptureConfigurationException if the device is messed up.
 *
 * JNI PacketCapture.getNetwork()
 */
JNIEXPORT jint JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_getNetwork
(JNIEnv *env, jobject obj, jstring jdevice) {
  char ebuf[PCAP_ERRBUF_SIZE];
  int localnet = 0;
  int netmask = 0;

  const char *device = env->GetStringUTFChars(jdevice, 0);

  if(pcap_lookupnet((char*)device,
                    (bpf_u_int32 *)&localnet,
                    (bpf_u_int32 *)&netmask, ebuf) < 0) {
    // if the lookup failed, throw an exception back to the java wrapper
    throwException(env, CONFIGURATION_EXCEPTION, ebuf);
    return 0;
  }
  else
    return localnet;
}

/*
 * Fetch the netmask associated with the device.
 * Throws a CaptureConfigurationException if the device is messed up.
 *
 * JNI PacketCapture.getNetmask()
 */
JNIEXPORT jint JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_getNetmask
(JNIEnv *env, jobject obj, jstring jdevice) {
  char ebuf[PCAP_ERRBUF_SIZE];
  const char *device = env->GetStringUTFChars(jdevice, 0);
  int localnet = 0;
  int netmask = 0;

  if(pcap_lookupnet((char*)device,
                    (bpf_u_int32*)&localnet,
                    (bpf_u_int32*)&netmask, ebuf) < 0) {
    // if the lookup failed, throw an exception back to the java wrapper
    throwException(env, CONFIGURATION_EXCEPTION, ebuf);
    return 0;
  }
  else
    return netmask;
}

/*
 * Fetch the link layer type associated with this device.
 *
 * JNI PacketCapture.getLinkLayerType()
 */
JNIEXPORT jint JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_getLinkLayerType
(JNIEnv *env, jobject obj, jint instance) {
  return pcap_datalink(PD[instance]);
}

/*
 * Create, compile and activate a filter from a filter expression.
 *
 * JNI PacketCapture.setFilter()
 */
JNIEXPORT void JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_setFilter
(JNIEnv *env, jobject object, jint instance, jstring jfilter, 
 jboolean optimize) {
  struct bpf_program bpp;
  const char *filter = env->GetStringUTFChars(jfilter, 0);

  // the device must be open in order to set the filter.
  if(PD[instance] == NULL) {
    throwException(env, INVALID_FILTER_EXCEPTION, 
                   "A device must be open before setting the filter.");
    return;
  }

  // compile bpf program
  if(pcap_compile(PD[instance], &bpp, (char*)filter, optimize, 0) == -1) {
    // if the filter wouldn't compile, throw an exception back to java
    throwException(env, INVALID_FILTER_EXCEPTION, pcap_geterr(PD[instance]));
    return;
  }

  // activate program
  if(pcap_setfilter(PD[instance], &bpp) == -1)
    // if the filter couldn't be activated, throw an exception back to java
    throwException(env, INVALID_FILTER_EXCEPTION, pcap_geterr(PD[instance]));
}

/*
 * Return the snapshot length being used (given network device has been 
 * opened) by using a pcap library API call.
 *
 * JNI PacketCapture.getSnapshotLength()
 */
JNIEXPORT jint JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_getSnapshotLength
  (JNIEnv *env, jobject obj, jint instance)
{
  int snapshotLength = -1;

  if(PD[instance] != NULL) {
    snapshotLength = pcap_snapshot(PD[instance]);
  }

  return snapshotLength;
}

/*
 * Close the capture device.
 *
 * JNI PacketCapture.close()
 */
JNIEXPORT void JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_close
(JNIEnv *env, jobject object, jint instance) {
  if(PD[instance] != NULL)
    pcap_close(PD[instance]);
}

/*
 * Fetch and set statistics in the java vm.
 *
 * JNI PacketCapture.setupStatistics()
 */
JNIEXPORT void JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_setupStatistics
(JNIEnv *env, jobject object, jint instance) {
  struct pcap_stat stat;

  if (PD[instance] != NULL && pcap_file(PD[instance]) == NULL) {
    if (pcap_stats(PD[instance], &stat) < 0) {
      /*
       * todo: throw the following as an exception..
       fprintf(stderr, "jpcap: pcap_stats(%s) %s\n", 
	 g_device, pcap_geterr(PD[instance]));
      */
    }
    else {
      jfieldID fid;
      jclass cls = env->GetObjectClass(object);
      // received count
      fid = env->GetFieldID(cls, "receivedCount", "I");
      if (fid == 0)
	return;
      env->SetIntField(object, fid, stat.ps_recv);
      // dropped count
      fid = env->GetFieldID(cls, "droppedCount", "I");
      if (fid == 0)
        return;
      env->SetIntField(object, fid, stat.ps_drop);
    }
  }
}

/*
 * This function is currently unused. might be used later by capture
 * to potentially adjust the snapshot length in the event that the 
 * capture client got it wrong.
 */
int gx_snaplen;
int adjustSnaplen(int verbose, int instance) {
  int i = -1;
  i = pcap_snapshot(PD[instance]);
  if(i == -1)
    return(0);
  if(i != gx_snaplen) {
    if(verbose) {
      printf("jpcap: snaplen was adjusted from %d to %d.\n", gx_snaplen, i);
      gx_snaplen = i;
    }
  } else {
    if(verbose)
      printf("jpcap: snaplen confirmed at %d.\n", gx_snaplen);
  }
  return(1);
}

/*
 * Class:     net_sourceforge_jpcap_capture_PacketCapture
 * Method:    lookupDevices
 * Signature: ()[Ljava/lang/String;
 */
JNIEXPORT jobjectArray JNICALL 
Java_net_sourceforge_jpcap_capture_PacketCapture_lookupDevices
(JNIEnv *env, jclass cls)
{
  char ebuf[PCAP_ERRBUF_SIZE];
  jobjectArray devices = NULL;


#ifndef WIN32
  int sock=socket(AF_INET,SOCK_DGRAM,0);
  struct ifconf ifc;
  struct ifreq *ifr,*last;
  struct ifreq ifrflags;
  pcap_t *pch;

  char names[100][100];
  int total = 0, i = 0, ifrSize = 0;

  if(sock < 0 ){
    /* error opening socket */
    throwException(env, DEVICE_LOOKUP_EXCEPTION, strerror(sock));
    return NULL;
  }

  ifc.ifc_len = 1024 * sizeof(struct ifreq);
  ifc.ifc_buf = (char *)malloc(ifc.ifc_len);

  if(ioctl(sock,SIOCGIFCONF,&ifc) < 0 ||
     ifc.ifc_len < (int)sizeof(struct ifreq)){
    /* SIOCGIFCONF error */
    goto FAIL;
  }

  ifr = (struct ifreq *)ifc.ifc_req;
  last = (struct ifreq *)((char *)ifr+ifc.ifc_len);

#ifdef HAVE_SA_LEN
    ifrSize = ifr->ifr_addr.sa_len+IFNAMSIZ;
#else /* HAVE_SA_LEN */
    ifrSize = sizeof(struct ifreq);
#endif /* HAVE_SA_LEN */

  char *s;
  for(;ifr < last; (char*)ifr += ifrSize, ifr=(struct ifreq *)s) {
    /* Skip "dummy" and "alaias" interface */
    /*
    if(strncmp(ifr->ifr_name,"dummy",5)==0 || 
       strchr(ifr->ifr_name,':') != NULL)
      continue;
    */

    for(i=0;i<total;i++)
      if(strcmp(names[i],ifr->ifr_name)==0)
	continue;

    /* Check flags */
    memset(&ifrflags,0,sizeof ifrflags);
    strncpy(ifrflags.ifr_name,ifr->ifr_name,sizeof ifrflags.ifr_name);
    if(ioctl(sock,SIOCGIFFLAGS,(char *)&ifrflags)<0){
      if(errno == ENXIO) 
        continue;
      else 
        goto FAIL;
    }

    if(!(ifrflags.ifr_flags & IFF_UP)) 
      continue;

    pch = pcap_open_live(ifr->ifr_name,68,0,0, ebuf);
    if(pch == NULL)
      continue;
    pcap_close(pch);
    strcpy(names[total++],ifr->ifr_name);
  }

  if( total > 0 )  {
    devices = env->NewObjectArray
      ((jsize)total, env->FindClass("java/lang/String"), NULL);
    for(i = 0 ; i < total ; i++ ) {
      env->SetObjectArrayElement(devices, i, env->NewStringUTF(names[i]));
    }
  }

FAIL:
  free(ifc.ifc_buf);
  close(sock);

#else /* WIN32 */
  wchar_t *dev;
  int i=0,c=0,j=0, t=0; // t = array index
  //char buf[256];
  //char buf2[256];
  char buf_all[516];
  char* desc = 0;
  dev = (wchar_t *)pcap_lookupdev(ebuf);
  if(dev){
    if(dev[0]<256) { /* NT / 2000 */
      if(dev[0]==0 && dev[1]==0)
        return NULL; /* no device */
      while(!(dev[i]==0 && dev[i-1]==0)){
        if(dev[i]==0) c++;
        i++;
      }

      // human-readable descriptions are placed after the device names
      desc = (char*)(dev + i + 1);

      devices=env->NewObjectArray
	((jsize)c, env->FindClass("java/lang/String"), NULL);
      //descriptions=env->NewObjectArray
      //  ((jsize)c, env->FindClass("java/lang/String"), NULL);

      i = 0;

      for(j=0; j<c; j++){
      /*
	//An attempt to set description strings within an array that was
	//passed as an argument .. still not sure how to do this.

        wcstombs(buf,(wchar_t *)(dev + i), 255);
        env->SetObjectArrayElement(devices, j, env->NewStringUTF(buf));
        wcstombs(buf2,(wchar_t *)(desc + t), 255);
        env->SetObjectArrayElement(descriptions, j, env->NewStringUTF(buf2));

        while(dev[i]!=0) {
          i++;
        }
        i++;

        while(desc[t] != 0) {
          t++;
        }
        t++;
       */

        // This code will get the device description as well as dev name
        // and put them both in the devices array
        t = 0;
        while (dev[i] != 0) {
          if (t < 255)
            buf_all[t++] = dev[i++];
        }
        i++;

        buf_all[t++] = '\n';
        buf_all[t++] = ' ';
        buf_all[t++] = ' '; // set "\n  " as windows signature

        while (*desc != 0) {
          if (t < 514)
	    buf_all[t++] = *desc;
          desc++;
        }
        buf_all[t++] = '\0';
        env->SetObjectArrayElement(devices, j, env->NewStringUTF(buf_all));
        desc++;
      }
    }else{ /* 9x */
      char *dev9x=(char *)dev;

      if(dev9x[0]==0 && dev9x[1]==0)
        return NULL; /* no device */
      while(!(dev9x[i]==0 && dev9x[i-1]==0)){
        if(dev9x[i]==0) c++;
        i++;
      }

      devices=env->NewObjectArray
        ((jsize)c, env->FindClass("java/lang/String"), NULL);
      i=0;
      for(j=0;j<c;j++){
        env->SetObjectArrayElement
          (devices, j, env->NewStringUTF((char *)(dev9x + i)));
	while(dev9x[i]!=0) i++;
	i++;
      }
    }
  }
#endif /* WIN32 */

  if(devices == NULL) {
      devices=env->NewObjectArray
        ((jsize)0, env->FindClass("java/lang/String"), NULL);
  }
  return devices;
}


const char *rcsid = 
  "$Id: jpcap.c,v 1.24 2004/10/07 18:04:41 pcharles Exp $";
