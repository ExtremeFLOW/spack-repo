# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Neko(AutotoolsPackage,CudaPackage,ROCmPackage):
    """N E K O"""

    homepage = "https://github.com/ExtremeFLOW/neko"
    git      = "https://github.com/ExtremeFLOW/neko.git"

    maintainers = ['njansson']

    version('0.3.0', tag='v0.3.0')
    version('0.2.2', tag='v0.2.2')
    version('0.2.1', tag='v0.2.1')
    version('0.2.0', tag='v0.2.0')
    version('0.1.3', tag='v0.1.3')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1.0', tag='v0.1.0')
    version('develop', branch='develop')
    variant('parmetis', default=False, description='Build with support for parmetis')
    variant('xsmm', default=False, description='Build with support for libxsmm')
    
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('pkgconf',  type='build')
    depends_on('parmetis', when='+parmetis')
    depends_on('libxsmm',  when='+xsmm')
    depends_on('mpi')
    depends_on('blas')
    depends_on('lapack')

    conflicts('+xsmm', when='+cuda')
    conflicts('+rocm', when='+cuda')

    def configure_args(self):
        args = []
        if '+parmetis' in self.spec:
            args.append('--with-parmetis')
        if '+xsmm' in self.spec:
            args.append('--with-libxsmm')
        if '+cuda' in self.spec:
            args.append('--with-cuda={0}'.format(self.spec['cuda'].prefix))
        if '+rocm' in self.spec:
            args.append('--with-hip={0}'.format(self.spec['hip'].prefix))

        return args
