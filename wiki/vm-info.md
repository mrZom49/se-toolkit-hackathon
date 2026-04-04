# Your VM image

<h2>Table of contents</h2>

- [Base image](#base-image)
- [Programs](#programs)
  - [`starship`](#starship)
  - [`ssh`](#ssh)
  - [`docker`](#docker)
  - [`git`](#git)
  - [`curl`](#curl)
  - [`nano`](#nano)
  - [`bash`](#bash)
  - [`uv`](#uv)
  - [`ripgrep`](#ripgrep)
  - [`python`](#python)
  - [`nix`](#nix)

## Base image

```terminal
Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-100-generic x86_64)
```

## Programs

### `starship`
  
Site: <https://github.com/starship/starship>

Version:

```terminal
starship --version
```

```terminal
starship 1.24.2
branch:master
commit_hash:33f7077
build_time:2025-12-30 19:14:09 +00:00
build_env:rustc 1.92.0 (ded5c06cf 2025-12-08),
```

### `ssh`
  
Version:

```terminal
ssh -V
```

```terminal
OpenSSH_9.6p1 Ubuntu-3ubuntu13.14, OpenSSL 3.0.13 30 Jan 2024
```

### `docker`

Site:

Version:

```terminal
docker --version
```

```terminal
Docker version 29.2.1, build a5c7197
```

### `git`

Version:

```terminal
git --version
```

```terminal
git version 2.43.0
```

### `curl`

Version:

```terminal
curl --version
```

```terminal
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.10
Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
```

### `nano`

Version:

```terminal
nano --version
```

```terminal
 GNU nano, version 7.2
 (C) 2023 the Free Software Foundation and various contributors
 Compiled options: --disable-libmagic --enable-utf8
```

### `bash`

> [!NOTE]
> This is the [login shell](./shell.md#login-shell).

Version:

```terminal
bash --version
```

```terminal
GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

### `uv`

Site: <https://docs.astral.sh/uv/>

Version:

```terminal
uv 0.10.1
```

### `ripgrep`

Site: <https://github.com/BurntSushi/ripgrep>

Version:

```terminal
rg --version
```

```terminal
ripgrep 14.1.0

features:-simd-accel,+pcre2
simd(compile):+SSE2,-SSSE3,-AVX2
simd(runtime):+SSE2,+SSSE3,+AVX2

PCRE2 10.42 is available (JIT is available)
```

### `python`

```terminal
python --version
```

<!-- TODO missing -->

### `nix`

Site: <https://github.com/DeterminateSystems/nix-installer#install-determinate-nix>

```terminal
nix --version
```

```terminal
nix (Determinate Nix 3.15.2) 2.33.1
```
