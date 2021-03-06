#ifndef ENCODE_VIDEO_H
#define ENCODE_VIDEO_H



#include <sys/types.h>

/** @file
 * @brief Encodes a series of frames as a video.
 *
 * Works by launching FFmpeg as a separate process and opening a pipe to it.
 * Encodes the video as HEVC. Each must be the wqme size and in the same image
 * format such as ppm.
 */

// switch between mp4 and webp
enum Encoder {MP4, MP4_RGB, WEBP, WEBP_SCALE, WEBP_LOSSY, GIF, GIF_SCALE};

/**
 * Launches FFmpeg by forking the current process and creates a pipe with it.
 * @param[in] fps Frames per seconds of the video
 * @param[in] filename Filename of the output video
 * @param[in] preset Determines encoding speed and quality
 * @param[out] outfd Write end of pipe
 * @param[out] pid pid of child process
 * @return -1 if an error occured, 0 otherwise
 */
int open_pipe(int fps, char* filename, enum Encoder encoder, int* outfd, pid_t* pid);

/**
 * Cleans up by closing the write end of the pipe and waits for the child to exit.
 * @param[in] outfd File descriptor for the write end of the pipe
 * @param[in] pid Pid of the child process
 */
void close_pipe(int outfd, pid_t pid);
#endif
