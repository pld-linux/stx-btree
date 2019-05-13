# NOTE: for legacy applications; new projects should use tlx
#
# Conditional build:
%bcond_without	wx	# wxWidgets based demo
#
Summary:	STX B+ Tree C++ template classes
Summary(pl.UTF-8):	Klasy szablonów STX implementujących B+-drzewa w C++
Name:		stx-btree
Version:	0.9
Release:	1
License:	Boost v1.0 (library), GPL v3 (demo and tests)
Group:		Libraries
Source0:	http://panthema.net/2007/stx-btree/%{name}-%{version}.tar.bz2
# Source0-md5:	823b16956c50d63040953962d720e837
URL:		http://panthema.net/2007/stx-btree/
%if %{with wx}
BuildRequires:	libstdc++-devel
BuildRequires:	wxGTK3-unicode-devel >= 2.6.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The STX B+ Tree package is a set of C++ template classes implementing
a B+ tree key/data container in main memory. The classes are designed
as drop-in replacements of the STL containers set, map, multiset and
multimap and follow their interfaces very closely. By packing
multiple value pairs into each node of the tree the B+ tree reduces
heap fragmentation and utilizes cache-line effects better than the
standard red-black binary tree. The tree algorithms are based on the
implementation in Cormen, Leiserson and Rivest's Introduction into
Algorithms, Jan Jannink's paper and other algorithm resources. The
classes contain extensive assertion and verification mechanisms to
ensure the implementation's correctness by testing the tree
invariants. To illustrate the B+ tree's structure a wxWidgets demo
program is included in %{name}-demo subpackage.

%description -l pl.UTF-8
Pakiet STX B+ Tree to zbiór klas szablonów C++ implementujących
kontenery B+-drzew klucz-wsartość w pamięci głównej. Klasy są
zaprojektowane jako zamienniki kontenerów STL: set, map, multiset i
multimap, z bardzo zbliżonymi interfejsami. Dzięki upakowaniu wielu
oar wartości w pojedynczym węźle B+-drzewa zmniejsza się fragmentacja
sterty i lepiej wykorzystywane są efekty wierszy pamięci podręcznej
niż w standardowych drzewach czerwono-czarnych. Algorytmy drzew są
oparte na "Wprowadzeniu do algorytmów" Cormena, Leisersona i Rivesta,
dokumencie Jana Janninka oraz innych źródłach. Klasy zawierają
obszerne mechanizmy zapewnień i weryfikacji, aby zapewnić poprawność
implementacji poprzez testowanie niezmienników drzewa. W celu
zilustrowania struktury drzew B+, załączony jest oparty na wxWidgets
program demonstracyjny (podpakiet %{name}-demo).

%package devel
Summary:	STX B+ Tree C++ template classes
Summary(pl.UTF-8):	Klasy szablonów STX implementujących B+-drzewa w C++
License:	Boost v1.0
Group:		Development/Libraries
Requires:	libstdc++-devel

%description devel
The STX B+ Tree package is a set of C++ template classes implementing
a B+ tree key/data container in main memory. The classes are designed
as drop-in replacements of the STL containers set, map, multiset and
multimap and follow their interfaces very closely. By packing
multiple value pairs into each node of the tree the B+ tree reduces
heap fragmentation and utilizes cache-line effects better than the
standard red-black binary tree. The tree algorithms are based on the
implementation in Cormen, Leiserson and Rivest's Introduction into
Algorithms, Jan Jannink's paper and other algorithm resources. The
classes contain extensive assertion and verification mechanisms to
ensure the implementation's correctness by testing the tree
invariants.

%description devel -l pl.UTF-8
Pakiet STX B+ Tree to zbiór klas szablonów C++ implementujących
kontenery B+-drzew klucz-wsartość w pamięci głównej. Klasy są
zaprojektowane jako zamienniki kontenerów STL: set, map, multiset i
multimap, z bardzo zbliżonymi interfejsami. Dzięki upakowaniu wielu
oar wartości w pojedynczym węźle B+-drzewa zmniejsza się fragmentacja
sterty i lepiej wykorzystywane są efekty wierszy pamięci podręcznej
niż w standardowych drzewach czerwono-czarnych. Algorytmy drzew są
oparte na "Wprowadzeniu do algorytmów" Cormena, Leisersona i Rivesta,
dokumencie Jana Janninka oraz innych źródłach. Klasy zawierają
obszerne mechanizmy zapewnień i weryfikacji, aby zapewnić poprawność
implementacji poprzez testowanie niezmienników drzewa.

%package demo
Summary:	STX B+ Tree demo GUI
Summary(pl.UTF-8):	Graficzny interfejs demonstracyjny do B+-drzew STX
License:	GPL v3
Group:		X11/Applications

%description demo
This demonstration program draws illustrations of the B+ trees
constructed by the STX B+ Tree template classes. The demo allows the
user to selected different types of B+ tree instantiations: integer or
string keys and different slot numbers. The user may insert and erase
key/data pairs from the tree and run different search operations. The
demo program uses the cross-platform wxWidgets toolkit.

%description demo -l pl.UTF-8
Ten program demonstracyjny rysuje ilustracje B+-drzew tworzonych przez
klasy szablonów STX implementujących B+-drzewa dla C++. Pozwala
użytkownikowi wybrać różne rodzaje instancji drzew B+: z kluczami
będącymi liczbami całkowitymi lub ciągami znaków oraz z różnymi
numerami slotów. Użytkownik może wstawiać i usuwać pary klucz-dane z
drzewa i uruchamiać różne operacje wyszukiwania. Program
demonstracyjny wykorzystuje wieloplatformowy toolkit wxWidgets.

%prep
%setup -q

%build
%configure \
	%{?with_wx:--with-wx-config=/usr/bin/wx-gtk3-unicode-config}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_includedir}/stx/btree.dox

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS README include/LICENSE_1_0.txt
%dir %{_includedir}/stx
%{_includedir}/stx/btree*

%if %{with wx}
%files demo
%defattr(644,root,root,755)
%doc wxbtreedemo/{AUTHORS,README}
%attr(755,root,root) %{_bindir}/wxBTreeDemo
%endif
