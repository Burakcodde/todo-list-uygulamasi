# Todo List Uygulaması

Bu proje, terminal tabanlı bir Todo List uygulamasıdır. Kullanıcılar görev ekleyebilir, listeleyebilir, silebilir ve tamamlayabilir. Görevler JSON formatında bir dosyaya kaydedilir ve uygulama başlatıldığında bu dosyadan yüklenir. Ayrıca, görevlerin öncelik seviyeleri ve tamamlanma tarihleri de takip edilir. Terminalde renkli ve güzel formatlanmış çıktılar elde etmek için `colorama` kütüphanesi kullanılmıştır.

## Özellikler

- Görev ekleme
- Görev listeleme
- Görev silme
- Görev tamamlama
- Görevlere öncelik seviyesi ekleme
- Görevlerin tamamlanma tarihini belirleme
- Görevleri JSON dosyasına kaydetme ve yükleme
- Terminalde renkli ve güzel formatlanmış çıktı

## Gereksinimler

- Python 3.x
- `colorama` kütüphanesi

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın veya indirin.
2. Gerekli Python kütüphanelerini yükleyin:

```sh
pip install colorama
```

Kullanım
Uygulamayı çalıştırmak için terminalde aşağıdaki komutu kullanın:

```sh
python todo.py
```

Uygulama başlatıldığında aşağıdaki menü ile karşılaşacaksınız:

```sh
Todo List Uygulaması
1. Görev Ekle
2. Görevleri Listele
3. Görev Sil
4. Görev Tamamla
5. Çıkış
Seçiminizi yapın:
```

Görev Ekleme
Görev eklemek için 1 tuşuna basın ve ardından eklemek istediğiniz görevi ve öncelik seviyesini girin.

Görevleri Listeleme
Görevleri listelemek için 2 tuşuna basın. Görevler, öncelik seviyeleri ve tamamlanma durumları ile birlikte listelenecektir.

Görev Silme
Görev silmek için 3 tuşuna basın ve ardından silmek istediğiniz görev numarasını girin.

Görev Tamamlama
Görev tamamlamak için 4 tuşuna basın ve ardından tamamlamak istediğiniz görev numarasını girin.

Çıkış
Uygulamadan çıkmak için 5 tuşuna basın.
