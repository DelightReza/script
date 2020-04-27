#!/usr/bin/env python
#encoding:utf8
#===============================================================================
#
#          FILE:  simg2img.py
# 
#         USAGE:  ./simg2img.py system.img 
# 
#   DESCRIPTION:  
# 
#        AUTHOR: Karl Zheng 
#       COMPANY: Meizu
#       CREATED: 2011年10月18日 15时25分15秒 CST
#      REVISION:  ---
#===============================================================================

import sys
import struct

class ext4_file_header:
	def __init__(self, buf):
		self.magic, \
				self.major, \
				self.minor, \
				self.file_header_size, \
				self.chunk_header_size, \
				self.block_size, \
				self.total_blocks, \
				self.total_chunks, \
				self.crc32, \
				= struct.unpack('<IHHHHIIII', buf)

class ext4_chunk_header:
	def __init__(self, buf):
		self.type,\
				self.reserved,\
				self.chunk_size,\
				self.total_size,\
				= struct.unpack('<HHII', buf)

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	print "Usage: simg2img.py input_file output_file"
	sys.exit(1)

if len(sys.argv) > 2:
	outfile = sys.argv[2]
else:
	print "No output file specified!"
	print "Usage: simg2img.py input_file output_file"
	sys.exit(1)

ifd = open(filename, "rb")

buf=""

# get filelen
ifd.seek(0, 2)
file_len = ifd.tell()
print file_len

EXT4_FILE_HEADER_MAGIC = 0xED26FF3A
EXT4_CHUNK_HEADER_SIZE = 12

magic_found=False
max_offs=min(file_len, 50*1024*1024) # don't look into the file more than 20Mb

# Very inefficient way to find the magic... but it's not too slow in practice so it's ok ;)
for k in xrange((file_len+3)/4):
	offs = k*4 # assumption: the magic value is aligned to 4 bytes
	ifd.seek(offs, 0)

	buf = ifd.read(28)
	#print repr(buf)
	file_header = ext4_file_header(buf)

	if file_header.magic == EXT4_FILE_HEADER_MAGIC:
		print "Found magic at offs=%(offs)d (0x%(offs)X)" % {'offs': offs}
		magic_found=True
		break

if not magic_found:
	print "Not a compressed ext4 file!!"
	sys.exit(1)

print "file_header chunks:%X"%(file_header.total_chunks)

total_chunks = file_header.total_chunks
print("total chunk = %d "%(total_chunks))

ofd = open(outfile, "wb")

sector_base = 82528
output_len = 0

while total_chunks > 0:
	buf = ifd.read(EXT4_CHUNK_HEADER_SIZE)
	chunk_header = ext4_chunk_header(buf)
	sector_size = (chunk_header.chunk_size * file_header.block_size) >> 9;
	#print "ct:%X, cs:%X, ts:%X, ss:%X"%(chunk_header.type, chunk_header.chunk_size, chunk_header.total_size, sector_size)

	data = ""
	if chunk_header.type == 0xCAC1:  # raw type 
		data = ifd.read(chunk_header.total_size - EXT4_CHUNK_HEADER_SIZE)
		if len(data) != (sector_size << 9):
			print("len data:%d, sector_size:%d"%(len(data), (sector_size << 9)))
			sys.exit(1)
		else:
			print ("len data:%d, sector_size:%d"%(len(data), sector_size << 9))
			ofd.write(data)
			output_len += len(data)
			print("raw_chunk ")
			print("write raw data in %d size %d \n"%(sector_base, sector_size))
			print("output len:%x"%(output_len))

			sector_base += sector_size
	else:
		if chunk_header.type == 0xCAC2:  # TYPE_FILL
			data = '\0' * (sector_size << 9);
			ofd.write(data) 
			output_len += len(data)
			print("fill_chunk \n")
			print("chunk_size:%x"%(chunk_header.chunk_size))
			print("output len:%x"%(output_len))
			sector_base += sector_size
		else:
			if chunk_header.type == 0xCAC3:  # TYPE_DONT_CARE
				print "none chunk at chunk:%d"%(file_header.total_chunks - total_chunks)
				print("data_size:0x%x, chunk_size:%d, block_size:%d"%(sector_size << 9, chunk_header.chunk_size, file_header.block_size))
				data = '\0' * (sector_size << 9);
				ofd.write(data) 
				output_len += len(data)
				sector_base += sector_size
			else:
				data = '\0' * (sector_size << 9);
				ofd.write(data)
				print "unknown type!!"
				output_len += len(data)
				print("output len:%x"%(output_len))
				sector_base += sector_size

	total_chunks -= 1 
	print("remain chunks = %d "%(total_chunks));

print "write done"

ifd.close()
ofd.close()


